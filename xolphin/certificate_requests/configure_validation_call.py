import json
import warnings

class ConfigureValidationCall(object):
    def __init__(self, request_id):
        self.request_id = request_id
        self._action = "ScheduledCallback"
        self._emailAddress = ""
        self.date = ""
        self.time = ""
        self.timezone = ""
        self.phoneNumber = ""
        self.extensionNumber = ""
        self.language = "en-us"
        self.comments = ""

    def toDict(self):
        result = {
            'request_id':self.request_id,
            'action':self.action,
            'date':self.date,
            'time':self.time,
            'timezone':self.timezone,
            'phoneNumber':self.phoneNumber,
            'extensionNumber':self.extensionNumber,
            'emailAddress':self.emailAddress,
            'language':self.language,
            'comments':self.comments,
        }
        return result

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self,value):
        actions = [ "ScheduledCallback", "ManualCallback", "ReplacePhone", "replaceEmailAddress","sendCallbackEmail"]
        if(value not in actions):
            raise Exception("Invalid action! Available actions: ScheduledCallback, ReplacePhone, replaceEmailAddress,sendCallbackEmail")

        self._action = value
    
    @property
    def language(self):
        return self._action

    @language.setter
    def language(self,value):
        languages = ['en-us', 'ru-ru', 'de-de', 'es-es', 'pt-br', 'nl-nl', 'fr-fr']
        if(value not in languages):
            raise Exception("Invalid languages! Available languages: 'en-us', 'ru-ru', 'de-de', 'es-es', 'pt-br', 'nl-nl', 'fr-fr'")

        self._action = value        

    @property
    def emailAddress(self):
        return self._emailAddress

    @emailAddress.setter
    def emailAddress(self,value):
        import re
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, value) == None):
            raise Exception("Invalid e-mail address")

        self._emailAddress = value 
