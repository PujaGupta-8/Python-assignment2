import logging.config

# Define formatters and handlers
VERBOSE_FORMATTER = {
    'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
}

SENSITIVE_FORMATTER = {
    'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
    'sensitive': True
}

CONSOLE_HANDLER = {
    'class': 'logging.StreamHandler',
    'level': 'DEBUG',
    'formatter': 'verbose'
}

FILE_HANDLER = {
    'class': 'logging.FileHandler',
    'filename': 'logs/myapp.log',
    'level': 'INFO',
    'formatter': 'verbose'
}

EMAIL_HANDLER = {
    'class': 'django.utils.log.AdminEmailHandler',
    'level': 'ERROR',
    'formatter': 'sensitive'
}

# Define logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': VERBOSE_FORMATTER,
        'sensitive': SENSITIVE_FORMATTER,
    },
    'handlers': {
        'console': CONSOLE_HANDLER,
        'file': FILE_HANDLER,
        'email': EMAIL_HANDLER,
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'myapp': {
            'handlers': ['console', 'file', 'email'],
            'level': 'DEBUG',
        },
        'myapp.module1': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'myapp.module2': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Configure logging
logging.config.dictConfig(LOGGING)