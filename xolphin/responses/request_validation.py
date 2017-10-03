from xolphin.responses.request_validation_domain import RequestValidationDomain


class RequestValidation(object):
    def __init__(self, data):
        self.status = data.get('status')
        self.status_detail = data.get('statusDetail')
        self.status_message = data.get('statusMessage')
        self.domains = [RequestValidationDomain(domain) for domain in data.get('domains', [])]
