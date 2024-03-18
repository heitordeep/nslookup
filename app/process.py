from services import Email

class Process:

    def __init__(self):
        self.services = [
            Email()
        ]

    def run_job(self, service, domain):
        return service.get_dns_information(domain)

    def get_service(self, input_service: str):
        for service in self.services:
            if service.check_service_exists(input_service):
                return service
        return
