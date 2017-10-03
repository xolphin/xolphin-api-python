from xolphin.responses.certificates import Certificates
from xolphin.responses.requests import Requests
from xolphin.responses.request import Request as Req
from xolphin.responses.certificate import Certificate as Cert


class Certificate(object):
    def __init__(self, client):
        self.client = client

    def all(self):
        certificates = []

        result = Certificates(self.client.get('certificates', {'page': 1}))
        if not result.is_error():
            certificates = result.certificates
            while result.page < result.pages:
                result = Certificates(self.client.get('certificates', {'page': result.page + 1}))
                if result.is_error():
                    break
                certificates = certificates + result.certificates

        return certificates

    def get(self, id):
        return Cert(self.client.get('certificates/%d' % id))

    def download(self, id, format='CRT'):
        result = self.client.download('certificates/%d/download' % id, {'format': format})
        return result.content

    def reissue(self, id, request):
        return Req(self.client.post('certificates/%d/reissue' % id, request.toDict()))

    def renew(self, id, request):
        return Req(self.client.post('certificates/%d/renew' % id, request.toDict()))

    def cancel(self, id, reason, revoke=False):
        return Req(self.client.post('certificates/%d/cancel' % id, {
            'reason': reason,
            'revoke': revoke
        }))
