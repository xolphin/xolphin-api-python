from xolphin.responses.base import Base
from xolphin.responses.request import Request


class Requests(Base):
    def __init__(self, data):
        super(Requests, self).__init__(data)

        if not self.is_error():
            self.requests = []
            for request in self._embedded['requests']:
                self.requests.append(Request(request))