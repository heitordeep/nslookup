import re

from control import Whois
from interface import ServicesInterface

class Email(ServicesInterface, Whois):

    def __init__(self):
        self.txt = 'include:spf.whservidor.com'

        self.protocol_with_entry_uol_host = (
            'pop.uhserver.com.',
            'service.uhserver.com.',
            'services.uhserver.com.',
            'mail.uhserver.com.',
            'imap.uhserver.com.',
            'smtp.uhserver.com.',
            'painel.dominiotemporario.com.',
        )

        self.protocol_no_entry_email_uol_host = (
            '10 mx.uhserver.com.',
            '0 mx.uhserver.com.',
        )

        self.protocol_no_entry_email_default = ('mx', 'txt')

        self.protocol_with_entry_email_default = (
            'imap',
            'pop',
            'pop3',
            'mail',
            'smtp',
            'painel',
            'webmail',
        )

        self.protocols_output = {}

    def check_service_exists(self, input_service: str) -> str:
        if input_service == 'E-MAIL PROFISSIONAL':
            return True
        return False

    def get_all_cnames(self, domain: str) -> None:
        
        for protocol in self.protocol_with_entry_email_default:

            output = self.get_cname(
                protocol=protocol,
                domain=domain
            )

            self.protocols_output.update(
                self.verification_dns(
                    output,
                    protocol,
                    domain,
                    self.protocol_with_entry_uol_host,
                )
            )

        return self

    def get_all_others_zones(self, domain: str) -> None:

        for protocol in self.protocol_no_entry_email_default:    
            
            output = self.get_other_zone(
                protocol=protocol,
                domain=domain
            )

            self.protocols_output.update(
                self.verification_dns(
                    output,
                    protocol,
                    domain,
                    self.protocol_no_entry_email_uol_host,
                )
            )
        
        return self
    
    def verification_dns(
        self, output, protocol, domain, equal_to_dns
    ):

        domain_results = {}
        protocol_to_sanitize = {}

        if output:

            protocol_to_sanitize = {
                'txt': output.split('\n'),
                'mx': output.split('\n'),
            }

            if output in equal_to_dns or output.count(self.txt):

                domain_results[protocol] = {
                    'entrada': f'{domain}',
                    'destino': protocol_to_sanitize.get(protocol, output),
                } # DNS zone correct

            else:
                domain_results[protocol] = {
                    'entrada': f'{domain}',
                    'destino': protocol_to_sanitize.get(protocol, output),
                    'error': 0,
                } # DNS zone incorrect
        else:
            domain_results[protocol] = {
                'entrada': f'{domain}',
                'destino': protocol_to_sanitize.get(protocol, output),
                'error': 1,
            } # DNS zone not found

        return domain_results
    
    def clear_domain(self, domain: str) -> str:
        self.domain_cleaned = re.sub(
            r"^(?:https?:\/\/)?(?:www\.)?", 
            '', 
            domain
        )
        return self

    def get_dns(self, domain: str) -> dict:
        self.clear_domain(domain)
        if not self.get_ns(self.domain_cleaned):
            return self.protocols_output
        (           
            self.get_all_cnames(domain=self.domain_cleaned)
            .get_all_others_zones(domain=self.domain_cleaned)
        )

        return self.protocols_output
