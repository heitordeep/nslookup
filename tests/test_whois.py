import pytest

from control import Whois


@pytest.fixture
def domain_list():
    return {
        'exists': [
            'udemy.com',
            'google.com.br',
        ],
        'not_exists': [
            'asdkkjasdasjd.com',
            'abcdsadaw342345.com'
        ]
    }

@pytest.fixture
def cname_list():
    return [
        'imap',
        'pop',
        'pop3',
        'mail',
        'smtp',
        'painel',
        'webmail',
    ]


def tests_whois(domain_list):
    whois = Whois()
    domain_exists = domain_list['exists']
    domain_not_exists = domain_list['not_exists']

    for domain in domain_exists:
        result = whois.get_ns(domain)
        assert result is True

    for domain in domain_not_exists:
        result = whois.get_ns(domain)
        assert result is False


def tests_cname(domain_list, cname_list):
    whois = Whois()
    domain_exists = domain_list['exists']
    domain_not_exists = domain_list['not_exists']

    for protocol in cname_list:
        for domain in domain_exists:
            cname_domain = whois.get_cname(protocol, domain)
            assert cname_domain is not None

    for protocol in cname_list:
        for domain in domain_not_exists:
            cname_domain = whois.get_cname(protocol, domain)
            assert cname_domain == ''


def tests_get_others_zone(domain_list, cname_list):
    whois = Whois()
    domain_exists = domain_list['exists']
    domain_not_exists = domain_list['not_exists']

    for protocol in cname_list:
        for domain in domain_exists:
            cname_domain = whois.get_other_zone(domain, protocol)
            assert cname_domain is not None

    for protocol in cname_list:
        for domain in domain_not_exists:
            cname_domain = whois.get_other_zone(domain, protocol)
            assert cname_domain == ''
