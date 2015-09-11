

class APIException(Exception):
    def __init__(self, error_code):
        Exception.__init__(self)
        self.error_code = error_code
