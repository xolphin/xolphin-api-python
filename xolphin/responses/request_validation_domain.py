class RequestValidationDomain(object):
    def __init__(self, data):
        if 'domain' in data: self.domain = data['domain']
        if 'dcvType' in data: self.dcv_type = data['dcvType']
        if 'dcvEmail' in data: self.dcv_email = data['dcvEmail']
        if 'status' in data: self.status = data['status']
        if 'statusDetail' in data: self.status_detail = data['statusDetail']
        if 'statusMessage' in data: self.status_message = data['statusMessage']