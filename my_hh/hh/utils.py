import functools
import operator
from datetime import date
from django.db.models import Q

from .models import Industry


def country_name_by_ISO_3166_1_alpha_2_code(code):
    """
    :param code: ISO 3166-1 alpha-2 (2-letter) code of the CIS country (Russia, Kazakhstan, Belarus, Uzbekistan,
    Azerbaijan, Georgia, Kyrgyzstan)
    :return: name of the country in English
    """
    country_dict = {
        'RU': 'Russia',
        'KZ': 'Kazakhstan',
        'BY': 'Belarus',
        'UZ': 'Uzbekistan',
        'AZ': 'Azerbaijan',
        'GE': 'Georgia',
        'KG': 'Kyrgyzstan',
    }
    return country_dict.get(code, None)


def salary_radio_value(salaryRadio):
    """
    :param salaryRadio: Salary value selected in the HTML select element
    :return: Minimum salary required
    """
    salary_dict = {
        '1': 0,
        '2': 40000,
        '3': 70000,
        '4': 150000,
        '5': 300000,
    }
    return salary_dict.get(salaryRadio, None)


def get_filter_kwargs(request, filter_list):
    """
    :param request: request
    :param filter_list: list of html names from request.GET
    :return: dictionary of filtered names which were in request.GET
    """

    filter_dict = {'search_bar': ('title__icontains', request.GET.get('search_bar', None)),
                   'part_time': ('is_part_time', True),
                   'remote': ('is_remote', True),
                   'country': ('country', request.GET.get('country', None)),
                   'city': ('city', request.GET.get('city', None)),
                   'industry': ('industry', Industry.objects.filter(title=request.GET.get('industry', None)).first()),
                   'salaryRadio': ('min_salary__gte', salary_radio_value(request.GET.get('salaryRadio', None))),
                   }
    filter_kwargs = {filter_dict[custom_filter][0]: filter_dict[custom_filter][1]
                     for custom_filter in filter_list if request.GET.get(custom_filter, None)}
    return filter_kwargs


def get_excluded_clauses(excluded_words_in_query):
    """
    :param request: request
    :return: Q object OR an empty list (if there were no words to exclude)
    """
    excluded_clauses = functools.reduce(operator.or_,
    (Q(title__icontains=word) for word in excluded_words_in_query),) \
        if len(excluded_words_in_query) > 0 else []
    return excluded_clauses


def calculate_age(date_of_birth):
    today = date.today()
    return today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))


def generate_post_dict(request):
    post_dict = {}
    for key in request.POST:
        if key == 'csrfmiddlewaretoken':
            pass
        else:
            key_name, key_id = key.split(':')
            if key_id not in post_dict:
                post_dict[key_id] = {}
            post_dict[key_id][key_name] = request.POST[key]
    return post_dict