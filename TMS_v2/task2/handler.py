CONSOLE_HANDLER = {
    'level': 'DEBUG',
    'class': 'logging.StreamHandler',
    'formatter': 'verbose',
}

FILE_HANDLER = {
    'level': 'DEBUG',
    'class': 'logging.handlers.RotatingFileHandler',
    'filename': 'django.log',
    'maxBytes': 1024*1024*10,  # 10MB
    'backupCount': 5,
    'formatter': 'verbose',
}

EMAIL_HANDLER = {
    'level': 'ERROR',
    'class': 'django.utils.log.AdminEmailHandler',
    'include_html': True,
}