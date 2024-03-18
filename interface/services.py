from abc import ABC, abstractclassmethod


class ServicesInterface(ABC):

    @abstractclassmethod
    def check_service_exists(self, input_service: str) -> str:
        pass

    @abstractclassmethod
    def get_all_cnames(self, domain: str) -> None:
        pass

    @abstractclassmethod
    def get_all_others_zones(self, domain: str) -> None:
        pass

    @abstractclassmethod
    def get_dns_information(self, domain: str) -> dict:
        pass
