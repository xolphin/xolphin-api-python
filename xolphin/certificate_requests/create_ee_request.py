import json

class CreateEERequest(object):
    def __init__(self):
        
        self.csr = ''
        self.approver_first_name = ''
        self.approver_last_name = ''
        self.approver_email = ''
        self.approver_phone = ''
        self.dcv_type = 'FILE'
        self.subject_alternative_names = []

    def toDict(self):
        result = {
            'csr': self.csr,
            'dcvType': self.dcv_type,
            'approverFirstName': self.approver_first_name,
            'approverLastName': self.approver_last_name,
            'approverEmail': self.approver_email,
            'approverPhone': self.approver_phone,
        }
        
        if len(self.subject_alternative_names) > 0: result['subjectAlternativeNames'] = ','.join(self.subject_alternative_names)

        return result
