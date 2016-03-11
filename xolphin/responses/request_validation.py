from xolphin.responses.request_validation_domain import RequestValidationDomain


class RequestValidation(object):
    def __init__(self, data):
        if 'status' in data: self.status = data['status']
        if 'statusDetail' in data: self.status_detail = data['statusDetail']
        if 'statusMessage' in data: self.status_message = data['statusMessage']

        if 'domains' in data:
            self.domains = []
            for domain in data['domains']:
                self.domains.append(RequestValidationDomain(domain))