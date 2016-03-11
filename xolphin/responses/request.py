from xolphin.responses.base import Base
from xolphin.responses.product import Product
from xolphin.responses.request_validation import RequestValidation


class Request(Base):
    def __init__(self, data):
        super(Request, self).__init__(data)

        if not self.is_error():
            if 'id' in data: self.id = data['id']
            if 'domainName' in data: self.domain_name = data['domainName']
            if 'subjectAlternativeNames' in data: self.subject_alternative_names = data['subjectAlternativeNames']
            if 'years' in data: self.years = data['years']
            if 'company' in data: self.company = data['company']
            if 'dateOrdered' in data: self.date_ordered = data['dateOrdered']
            if 'department' in data: self.department = data['department']
            if 'address' in data: self.address = data['address']
            if 'zipcode' in data: self.zipcode = data['zipcode']
            if 'city' in data: self.city = data['city']
            if 'province' in data: self.province = data['province']
            if 'country' in data: self.country = data['country']
            if 'reference' in data: self.reference = data['reference']
            if 'approverFirstName' in data: self.approver_first_name = data['approverFirstName']
            if 'approverLastName' in data: self.approver_last_name = data['approverLastName']
            if 'approverEmail' in data: self.approver_email = data['approverEmail']
            if 'approverPhone' in data: self.approver_phone = data['approverPhone']
            if 'kvk' in data: self.kvk = data['kvk']

            if 'validations' in data:
                self.validations = {}

                for k in data['validations']:
                    self.validations[k] = RequestValidation(data['validations'][k])

            if ('_embedded' in data) and ('product' in data['_embedded']):
                self.product = Product(data['_embedded']['product'])