class BaseAppException(Exception):
    def __init__(self, is_error: bool, results: str, message_template: str):
        self.is_error = is_error
        self.results = results
        self.message = message_template.format(results)  # replace message template placeholders {} by the results value
