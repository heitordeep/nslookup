from typing import Dict

from domain import DomainService
from ports import WhoisPort
from share import Protocols


class ServiceApplication:
    
    def __init__(self, whois: WhoisPort) -> None:
        self.whois = whois
        self.service = DomainService()

    def __domain_info(self, domain: str) -> Dict:
        dns_info = dict()
        for protocol in Protocols.get(): 
            dns_info[protocol] = self.whois.get_cname(protocol, domain)

        for protocol in Protocols.get_other_protocols():
            dns_info[protocol] = (
                self.whois.get_other_zone(protocol, domain)
            )
        return dns_info
    
    def get_dns(self, domain: str) -> Dict:
        domain = self.service.sanitize_domain(domain)
        
        if not domain:
            return 'Domain not specified'

        if not self.whois.get_ns(domain):
            return f'{domain} NS not found'
        
        
        domain_info = self.__domain_info(domain)
        return self.service.verification_dns(domain, domain_info)
