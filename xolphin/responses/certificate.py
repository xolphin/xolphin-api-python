from xolphin.responses.base import Base
from xolphin.responses.product import Product
import datetime

class Certificate(Base):
    def __init__(self, data):
        super(Certificate, self).__init__(data)

        if not self.is_error():
            if 'id' in data: self.id = data['id']
            if 'domainName' in data: self.domain_name = data['domainName']
            if 'subjectAlternativeNames' in data: self.subject_alternative_names = data['subjectAlternativeNames']
            if 'dateIssued' in data: self.date_issued = datetime.datetime.strptime(data['dateIssued'].split('T')[0], '%Y-%m-%d')
            if 'dateExpired' in data: self.date_expired = datetime.datetime.strptime(data['dateExpired'].split('T')[0], '%Y-%m-%d')
            if 'company' in data: self.company = data['company']
            if 'customerId' in data: self.customer_id = data['customerId']

            if ('_embedded' in data) and ('product' in data['_embedded']):
                self.product = Product(data['_embedded']['product'])

    def isExpired(self):
        return self.date_expired <= datetime.datetime.now()