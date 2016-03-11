from xolphin.responses.base import Base
from xolphin.responses.product_price import ProductPrice


class Product(Base):
    def __init__(self, data):
        super(Product, self).__init__(data)

        if not self.is_error():
            if 'id' in data: self.id = data['id']
            if 'brand' in data: self.brand = data['brand']
            if 'name' in data: self.name = data['name']
            if 'type' in data: self.type = data['type']
            if 'validation' in data: self.validation = data['validation']
            if 'includeDomains' in data: self.include_domains = data['includeDomains']
            if 'maxDomains' in data: self.max_domains = data['maxDomains']

            if 'prices' in data:
                self.prices = []
                for v in data['prices']:
                    self.prices.append(ProductPrice(v))
