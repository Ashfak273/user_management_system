class DbOperationException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)  # pass the error message to the base Exception
        self.errors = errors
