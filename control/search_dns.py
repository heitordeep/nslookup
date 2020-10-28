import subprocess


class Whois:
    def __init__(self):
        self.txt = 'include:spf.whservidor.com'

    def consult_ns(self, domain):

        proc = subprocess.Popen(
            f'dig {domain} ns +short',
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )
        try:
            outs, errs = proc.communicate(timeout=20)
            if outs.decode('utf-8') != '':
                return True
            return False

        except TimeoutExpired:
            outs, errs = proc.communicate()
            proc.kill()

    def email_profissional(self, domain, zone):

        protocol_with_entry_uol_host = [
            'pop.uhserver.com.',
            'service.uhserver.com.',
            'services.uhserver.com.',
            'mail.uhserver.com.',
            'imap.uhserver.com.',
            'smtp.uhserver.com.',
            'painel.dominiotemporario.com.',
        ]

        protocol_no_entry_email_uol_host = [
            '10 mx.uhserver.com.',
            '0 mx.uhserver.com.',
        ]

        protocol_no_entry_email_default = ['mx', 'txt']

        protocol_with_entry_email_default = [
            'imap',
            'pop',
            'pop3',
            'mail',
            'smtp',
            'painel',
            'webmail',
        ]

        protocols_output = {}
        for protocol in (
            protocol_with_entry_email_default + protocol_no_entry_email_default
        ):

            if protocol in protocol_with_entry_email_default:

                output = subprocess.getoutput(
                    f'dig {protocol}.{domain} cname +short'
                )

                protocols_output.update(
                    self.verification_dns(
                        output,
                        protocol,
                        domain,
                        protocol_with_entry_email_default,
                        protocol_with_entry_uol_host,
                    )
                )

            else:

                output = subprocess.getoutput(
                    f'dig {domain} {protocol} +short'
                )

                protocols_output.update(
                    self.verification_dns(
                        output,
                        protocol,
                        domain,
                        protocol_no_entry_email_default,
                        protocol_no_entry_email_uol_host,
                    )
                )

        return protocols_output

    def verification_dns(
        self, output, protocol, domain, entry_uol_host, equal_to_dns
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
                }
        else:
            domain_results[protocol] = {
                'entrada': f'{domain}',
                'destino': protocol_to_sanitize.get(protocol, output),
                'error': 1,
            }

        return domain_results
