from xolphin.responses.base import Base
from xolphin.responses.product import Product
from xolphin.responses.request_validation import RequestValidation


class RequestEE(Base):
    def __init__(self, data):
        super(RequestEE, self).__init__(data)
        if not self.is_error():
            if 'id' in data: self.id = data['id']
            if 'dateOrdered' in data: self.date_ordered = data['dateOrdered']
            if 'pkcs7' in data: self.pkcs7 = data['pkcs7']
            if 'crt' in data: self.crt = data['crt']
