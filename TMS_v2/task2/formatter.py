VERBOSE_FORMATTER = {
    'format': '{levelname} {asctime} {module} {message}',
    'style': '{',
}

SENSITIVE_FORMATTER = {
    '()': 'path.to.SensitiveDataFormatter',  # Update this to point to your SensitiveDataFormatter class
    'format': '{levelname} {asctime} {module} {message}',
    'style': '{',
}