from xolphin.certificate_requests.create_certificate_request import CreateCertificateRequest
from xolphin.certificate_requests.create_ee_request import CreateEERequest
from xolphin.responses.base import Base
from xolphin.responses.requests import Requests
from xolphin.responses.request import Request as Req
from xolphin.responses.request_ee import RequestEE as ReqEE
from xolphin.responses.notes import Notes


class Request(object):
    def __init__(self, client):
        self.client = client

    def all(self):
        requests = []

        result = Requests(self.client.get('requests', {'page': 1}))
        if not result.is_error():
            requests = result.requests
            while result.page < result.pages:
                result = Requests(self.client.get('requests', {'page': result.page + 1}))
                if result.is_error():
                    break
                requests = requests + result.requests

        return requests

    def create(self, product, years, csr, dcv_type):
        return CreateCertificateRequest(product, years, csr, dcv_type)
    
    def create_ee(self):
        return CreateEERequest()

    def send(self, request):
        return Req(self.client.post('requests', request.toDict()))

    def send_ee(self, request):
        return ReqEE(self.client.post('requests/ee', request.toDict()))

    def get(self, id):
        return Req(self.client.get('requests/%d' % id))

    def upload_document(self, id, document, description):
        return Base(self.client.post('requests/%d/upload-document' % id, {
            'document': document,
            'description': description
        }))

    def retry_dcv(self, id, domain, dcv_type, email=''):
        return Base(self.client.post('requests/%d/retry-dcv' % id, {
            'domain': domain,
            'dcvType': dcv_type,
            'email': email
        }))

    def send_subscriber_agreement(self, id, email, language = ""):
        return Base(self.client.post('requests/%d/sa' % id, {
            'email': email,
            'language': language
        }))

    def schedule_validation_call(self, id, date_time):
        return Base(self.client.post('requests/%d/schedule-validation-call' % id, {
            'date': date_time.strftime('%Y-%m-%d'),
            'time': date_time.strftime('%H:%M')
        }))

    def send_note(self, id, message):
        return Base(self.client.post('requests/%d/notes' % id, {
            'message': message
        }))

    def get_notes(self, id):
        notes = []

        result = Notes(self.client.get('requests/%d/notes' % id))
        if not result.is_error():
            notes = result.notes
        
        return notes

    def send_ComodoSA(self, id, to, language = ""):
        return Base(self.client.post('requests/%d/sa' % id, {
            'sa_email': to,
            'language': language,
        }))
