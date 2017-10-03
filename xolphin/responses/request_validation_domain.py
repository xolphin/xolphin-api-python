class RequestValidationDomain(object):
    def __init__(self, data):
        if 'domain' in data: self.domain = data['domain']
        if 'dcvType' in data: self.dcv_type = data['dcvType']
        if 'dcvEmail' in data: self.dcv_email = data['dcvEmail']
        if 'status' in data: self.status = data['status']
        if 'statusDetail' in data: self.status_detail = data['statusDetail']
        if 'statusMessage' in data: self.status_message = data['statusMessage']
        if 'md5' in data: self.md5 = data['md5']
        if 'sha1' in data: self.sha1 = data['sha1']

        if 'dnsRecord' in data: self.dnsRecord = data['dnsRecord']
        if 'dnsCnameValue' in data: self.dnsCnameValue = data['dnsCnameValue']
        if 'fileLocation' in data: self.fileLocation = data['fileLocation']
        if 'fileContents' in data: self.fileContents = data['fileContents']
