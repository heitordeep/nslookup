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
