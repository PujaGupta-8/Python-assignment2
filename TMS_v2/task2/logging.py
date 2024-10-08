import re
from logging import Filter

class MaskSensitiveDataFilter(Filter):
    """
    Logging filter to mask sensitive data in log messages.
    """

    SENSITIVE_FIELDS = ['password', 'token', 'key']

    def filter(self, record):
        record.msg = self.mask_sensitive_data(record.msg)
        return True

    def mask_sensitive_data(self, message):
        for field in self.SENSITIVE_FIELDS:
            message = re.sub(f'({field}=)([^&\\s]+)', r'\1[REDACTED]', message, flags=re.IGNORECASE)
        return message