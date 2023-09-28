
def country_name_by_ISO_3166_1_alpha_2_code(code):
    """
    :param code: ISO 3166-1 alpha-2 (2-letter) code of the CIS country (Russia, Kazakhstan, Belarus, Uzbekistan,
    Azerbaijan, Georgia, Kyrgyzstan)
    :return: name of the country in english
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


def salary_radio_results(salaryRadio):
    """
    :param salaryRadio: Salary radio value from request.POST
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


def pipi(popo):
    return None

