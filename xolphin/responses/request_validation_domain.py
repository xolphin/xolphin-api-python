class RequestValidationDomain(object):
    def __init__(self, data):
        self.domain = data.get('domain')
        self.dcv_type = data.get('dcvType')
        self.dcv_email = data.get('dcvEmail')
        self.status = data.get('status')
        self.status_detail = data.get('statusDetail')
        self.status_message = data.get('statusMessage')
        self.md5 = data.get('md5')
        self.sha1 = data.get('sha1')
