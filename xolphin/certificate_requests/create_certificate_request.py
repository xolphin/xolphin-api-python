import json

class CreateCertificateRequest(object):
    def __init__(self, product, years, csr, dcv_type):
        self.product = product
        self.years = years
        self.csr = csr
        self.dcv_type = dcv_type

        self.subject_alternative_names = []
        self.dcv = []
        self.company = ''
        self.department = ''
        self.address = ''
        self.zipcode = ''
        self.city = ''
        self.approver_first_name = ''
        self.approver_last_name = ''
        self.approver_email = ''
        self.approver_phone = ''
        self.kvk = ''
        self.reference = ''

    def toDict(self):
        result = {
            'product': self.product,
            'years': self.years,
            'csr': self.csr,
            'dcvType': self.dcv_type,
        }
        
        if len(self.subject_alternative_names) > 0: result['subjectAlternativeNames'] = ','.join(self.subject_alternative_names)
        if len(self.dcv) > 0: result['dcv'] = json.dumps(self.dcv)

        if self.company != '': result['company'] = self.company
        if self.department != '': result['department'] = self.department
        if self.address != '': result['address'] = self.address
        if self.zipcode != '': result['zipcode'] = self.zipcode
        if self.city != '': result['city'] = self.city
        if self.approver_first_name != '': result['approverFirstName'] = self.approver_first_name
        if self.approver_last_name != '': result['approverLastName'] = self.approver_last_name
        if self.approver_email != '': result['approverEmail'] = self.approver_email
        if self.approver_phone != '': result['approverPhone'] = self.approver_phone
        if self.kvk != '': result['kvk'] = self.kvk
        if self.reference != '': result['reference'] = self.reference
        
        return result
