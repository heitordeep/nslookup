from abc import ABC, abstractclassmethod
from typing import Dict


class ServicesInterface(ABC):

    @abstractclassmethod
    def get_all_cnames(self, domain: str) -> None:
        pass

    @abstractclassmethod
    def get_all_others_zones(self, domain: str) -> None:
        pass

    @abstractclassmethod
    def get_dns_information(self, domain: str) -> Dict:
        pass
