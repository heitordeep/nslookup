from services import Email 

class Process:

    def __init__(self) -> None:
        self.services = [
            Email()
        ]

    def run_job(self, service, domain):
        return service.get_dns(domain)

    def get_service(self, input_service: str) -> None:
        for service in self.services:
            if service.check_service_exists(input_service):
                return service
        return
