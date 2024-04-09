from typing import Tuple


class Protocols:
    @staticmethod
    def get() -> Tuple:
        return (
            'pop',
            'service',
            'services',
            'mail',
            'imap',
            'smtp',
            'painel',
            'webmail'
        )
    
    @staticmethod
    def get_other_protocols():
        return ('txt', 'mx')
