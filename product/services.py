from product.email import Email

class Process:

    def __init__(self) -> None:
        self.products = [
            Email
        ]

    def consult_product(self, input_product: str) -> None:
        for product in self.products:
            job = product()
            if job.__str__() == input_product:
                return job
        
        raise Exception(f'{input_product} product does not exists')

