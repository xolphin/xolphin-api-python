from xolphin.responses.certificate import Certificate
from xolphin.responses.base import Base


class Certificates(Base):
    def __init__(self, data):
        super(Certificates, self).__init__(data)

        if not self.is_error():
            self.certificates = []
            for certificate in self._embedded['certificates']:
                self.certificates.append(Certificate(certificate))