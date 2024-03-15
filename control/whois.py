import subprocess


class Whois:

    def consult_ns(self, domain: str) -> bool:

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

        except subprocess.TimeoutExpired:
            outs, errs = proc.communicate()
            proc.kill()

    def consult_cname(self, protocol: str, domain:str) -> str:
        return subprocess.getoutput(
            f'dig {protocol}.{domain} cname +short'
        )

    def consult_other_zone(self, domain: str, protocol: str) -> str:
        return subprocess.getoutput(
            f'dig {domain} {protocol} +short'
        )