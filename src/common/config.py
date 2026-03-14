import os
from src.infrastructure.constants import LOGGING_DIR

os.makedirs(LOGGING_DIR, exist_ok=True)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "mode": "a",
            "filename": os.path.join(LOGGING_DIR, "lab.log"),
            "maxBytes": 5 * 1024 * 1024,  # 5 MB before rotating
            "backupCount": 5,
            "level": "DEBUG",
            "encoding": "utf-8"
        },
    },
    "loggers": {
        "": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": True,
        }
    },
}