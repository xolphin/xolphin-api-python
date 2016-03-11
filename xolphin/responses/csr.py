from xolphin.responses.base import Base


class CSR(Base):
    def __init__(self, data):
        super(CSR, self).__init__(data)

        if not self.is_error():
            if 'type' in data: self.type = data['type']
            if 'size' in data: self.size = data['size']
            if 'company' in data: self.company = data['company']
            if 'cn' in data: self.cn = data['cn']
            if 'state' in data: self.state = data['state']
            if 'city' in data: self.city = data['city']
            if 'country' in data: self.country = data['country']
            if 'altNames' in data: self.altNames = data['altNames']
