import re
from typing import Dict, List


class DomainService:

    def __init__(self):
        self.default_txt_entry = 'include:spf.whservidor.com'
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
        """Remove 'http', 'https', 'www', and '/' from domain"""
        return re.sub(r'https?://(?:www\.)?|www\.|/', '', domain)
    
    def __is_valid_dns(self, server: str) -> bool:
        """Check if the DNS server is valid"""
        return (
            server in self.protocol_with_entry_uol_host 
            or server in self.protocol_no_entry_email_uol_host
            or server.count(self.default_txt_entry)
        )
    
    def __sanitize_server(self, server: str) -> str:
        return server.replace('"', '').split('\n') if server else {}

    def verification_dns(
        self, domain: str, dns_info: Dict[str, str]
    ) -> Dict[str, List]:
        """Verify DNS entries."""
        domain_results = {}

        for protocol, server in dns_info.items():

            error_flag = 0 if server else 1
            domain_results[protocol] = {
                'entrada': domain,
                'destino': self.__sanitize_server(server),
            }

            if not self.__is_valid_dns(server):
                # DNS zone not found or zone incorrect
                domain_results[protocol]['error'] = error_flag

        return domain_results
