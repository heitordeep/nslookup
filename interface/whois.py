from abc import ABC, abstractclassmethod

class WhoisInterface(ABC):

    @abstractclassmethod
    def get_ns(self, domain: str) -> bool:
        pass

    @abstractclassmethod
    def get_cname(self, protocol: str, domain:str) -> str:
        pass

    @abstractclassmethod
    def get_other_zone(self, domain: str, protocol: str) -> str:
        pass