import re
from typing import Dict


class DomainService:

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

        self.protocols_output = {}

    @staticmethod
    def sanitize_domain(domain: str) -> str:
        return re.sub(
            r'https?://(?:www\.)?|www\.|/',
            '', 
            domain
        )

    def verification_dns(self, domain: str, dns_info: Dict) -> Dict:
        domain_results = {}
        protocol_to_sanitize = {}

        for protocol, server in dns_info.items():
            if server:
                protocol_to_sanitize = {
                    'txt': server.split('\n'),
                    'mx': server.split('\n'),
                }
                if (
                    server in self.protocol_with_entry_uol_host 
                    or 
                    server in self.protocol_no_entry_email_uol_host
                    or
                    server.count(self.txt)
                ):
                    domain_results[protocol] = {
                        'entrada': domain,
                        'destino': protocol_to_sanitize.get(protocol, server),
                    } # DNS zone correct
                else:
                    domain_results[protocol] = {
                        'entrada': domain,
                        'destino': protocol_to_sanitize.get(protocol, server),
                        'error': 0,
                    } # DNS zone incorrect
            else:
                domain_results[protocol] = {
                    'entrada': domain,
                    'destino': protocol_to_sanitize.get(protocol, server),
                    'error': 1,
                } # DNS zone not found

        return domain_results
