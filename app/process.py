from typing import Dict, Union

from interface import ServicesInterface
from services import Email


class Process:

    def __init__(self) -> None:
        self.services: Dict = {
            'E-MAIL PROFISSIONAL': Email()
        }

    def run_job(self, service, domain) -> ServicesInterface:
        return service.get_dns_information(domain)

    def get_service(
        self, 
        input_service: str
    ) -> Union[ServicesInterface, None]:
    
        if input_service in self.services.keys():
            return self.services[input_service]
        return

    def process_request(self, domain: str, service: str) -> Union[Dict, str]:
        service_whois = self.get_service(service)
        if not service_whois:
            return f'Serviço {service} não existe'

        domain_ns = self.run_job(service_whois, domain)
        if not domain_ns:
            return f'Domínio {domain} não existe'

        return domain_ns
