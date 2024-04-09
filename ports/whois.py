from abc import ABC, abstractclassmethod


class WhoisPort(ABC):

    @abstractclassmethod
    def get_ns(self, domain: str) -> bool:
        pass

    @abstractclassmethod
    def get_cname(self, protocol: str, domain:str) -> str:
        pass

    @abstractclassmethod
    def get_other_zone(self, protocol: str, domain: str) -> str:
        pass
