import json
import warnings

class CreateEERequest(object):
    def __init__(self):
        
        self.csr = ''
        self.approver_first_name = ''
        self.approver_last_name = ''
        self.approver_email = ''
        self.approver_phone = ''
        self.approver_representative_first_name = ''
        self.approver_representative_last_name = ''
        self.approver_representative_email = ''
        self.approver_representative_phone = ''
        self.approver_representative_position = ''

        self.dcv_type = 'FILE'
        self.subject_alternative_names = []

    def toDict(self):
        result = {
            'csr': self.csr,
            'dcvType': self.dcv_type,
        }

        if len(self.subject_alternative_names) > 0: result['subjectAlternativeNames'] = ','.join(self.subject_alternative_names)

        if self.approver_first_name != '': result['approverFirstName'] = self.approver_first_name
        if self.approver_last_name != '': result['approverLastName'] = self.approver_last_name
        if self.approver_email != '': result['approverEmail'] = self.approver_email
        if self.approver_phone != '': result['approverPhone'] = self.approver_phone
        
        if self.approver_representative_first_name != '': result['approverRepresentativeFirstName'] = self.approver_representative_first_name
        if self.approver_representative_last_name != '': result['approverRepresentativeLastName'] = self.approver_representative_last_name
        if self.approver_representative_email != '': result['approverRepresentativeEmail'] = self.approver_representative_email
        if self.approver_representative_phone != '': result['approverRepresentativePhone'] = self.approver_representative_phone
        if self.approver_representative_position != '': result['approverRepresentativePosition'] = self.approver_representative_position


        return result

    @property        
    def approver_first_name(self):
        return self._approver_first_name
    @property    
    def approver_last_name(self):
        return self._approver_last_name
    @property    
    def approver_phone(self):
        return self._approver_phone


    @approver_first_name.setter
    def approver_first_name(self,value):
        self._approver_first_name = value
        if(value != ''):
            warnings.warn("Warning! approverFirstName is deprecated, please use approverRepresentativeFirstName")

    @approver_last_name.setter
    def approver_last_name(self,value):
        self._approver_last_name = value
        if(value != ''):
            warnings.warn("Warning! approverLastName is deprecated, please use approverRepresentativeLastName")

    @approver_phone.setter
    def approver_phone(self,value):
        self._approver_phone = value
        if(value != ''):
            warnings.warn("Warning! approverPhone is deprecated, please use approverRepresentativePhone")
