from xolphin.responses.base import Base

class Note(Base):
    def __init__(self, data):
        super(Note, self).__init__(data)

        if not self.is_error():
            if 'contact' in data: self.contact = data['contact']
            if 'staff' in data: self.staff = data['staff']
            if 'date' in data: self.date = data['date']
            if 'time' in data: self.time = data['time']
            if 'message' in data: self.messageBody = data['message']
            if 'createdAt' in data: self.createdAt = data['createdAt']
