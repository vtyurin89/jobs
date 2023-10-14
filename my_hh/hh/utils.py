from datetime import date
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
    :param filter_list: list of html names from request.POST
    :return: dictionary of filtered names which were in request.POST
    """

    filter_dict = {'search_bar': ('title__icontains', request.POST.get('search_bar', None)),
                   'part_time': ('is_part_time', True),
                   'remote': ('is_remote', True),
                   'country': ('country', request.POST.get('country', None)),
                   'city': ('city', request.POST.get('city', None)),
                   'industry': ('industry', Industry.objects.filter(title=request.POST.get('industry', None)).first()),
                   'salaryRadio': ('min_salary__gte', salary_radio_value(request.POST.get('salaryRadio', None))),
                   }
    filter_kwargs = {filter_dict[custom_filter][0]: filter_dict[custom_filter][1]
                     for custom_filter in filter_list if request.POST.get(custom_filter, None)}
    return filter_kwargs


def calculate_age(date_of_birth):
    today = date.today()
    return today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))