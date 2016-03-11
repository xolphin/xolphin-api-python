class Base(object):
    def __init__(self, data):
        if 'message' in data:
            self.message = data['message']

        if 'errors' in data:
            self.errors = data['errors']

        if 'page' in data:
            self.page = data['page']
            self.pages = data['pages']
            self.limit = data['limit']
            self.total = data['total']

        if '_embedded' in data:
            self._embedded = data['_embedded']

    def is_error(self):
        if hasattr(self, 'errors'):
            return True
        else:
            return False

    def get_error_message(self):
        return self.message

    def get_error_data(self):
        return self.errors