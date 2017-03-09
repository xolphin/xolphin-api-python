from xolphin.responses.base import Base
from xolphin.responses.note import Note


class Notes(Base):
    def __init__(self, data):
        super(Notes, self).__init__(data)

        if not self.is_error():
            self.notes = []
            for note in self._embedded['notes']:
                self.notes.append(Note(note))
