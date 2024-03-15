from control.whois import Whois

class Email(Whois):

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

    def __str__(self) -> str:
        return 'E-MAIL PROFISSIONAL'

    def __get_cname(self, domain: str) -> None:
        
        for protocol in self.protocol_with_entry_email_default:

            output = self.consult_cname(
                protocol=protocol,
                domain=domain
            )

            self.protocols_output.update(
                self.__verification_dns(
                    output,
                    protocol,
                    domain,
                    self.protocol_with_entry_uol_host,
                )
            )

        return self

    def __get_others_zones(self, domain: str) -> None:

        for protocol in self.protocol_no_entry_email_default:    
            
            output = self.consult_other_zone(
                protocol=protocol,
                domain=domain
            )

            self.protocols_output.update(
                self.__verification_dns(
                    output,
                    protocol,
                    domain,
                    self.protocol_no_entry_email_uol_host,
                )
            )
        
        return self
    
    def __verification_dns(
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
                }

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


    def consult_email(self, domain: str) -> dict:
        (
            self.__get_cname(domain=domain)
            .__get_others_zones(domain=domain)
        )

        return self.protocols_output
