from xolphin.responses.base import Base
from xolphin.responses.product import Product


class Products(Base):
    def __init__(self, data):
        super(Products, self).__init__(data)

        if not self.is_error():
            self.products = []
            for product in self._embedded['products']:
                self.products.append(Product(product))
