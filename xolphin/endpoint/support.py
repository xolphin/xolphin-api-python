from xolphin.certificate_requests.create_certificate_request import CreateCertificateRequest
from xolphin.responses.base import Base
from xolphin.responses.certificates import Certificates
from xolphin.responses.csr import CSR
from xolphin.responses.product import Product
from xolphin.responses.products import Products
from xolphin.responses.requests import Requests
from xolphin.responses.request import Request as Req


class Support(object):
    def __init__(self, client):
        self.client = client

    def products(self):
        products = []

        result = Products(self.client.get('products', {'page': 1}))
        if not result.is_error():
            products = result.products
            while result.page < result.pages:
                result = Products(self.client.get('products', {'page': result.page + 1}))
                if result.is_error():
                    break
                products = products + result.products

        return products

    def product(self, id):
        return Product(self.client.get('products/%d' % id))

    def decode_csr(self, csr):
        return CSR(self.client.post('decode-csr', {
            'csr': csr
        }))

    def approver_email_addresses(self, domain):
        return self.client.get('approver-email-addresses', {
            'domain': domain
        })