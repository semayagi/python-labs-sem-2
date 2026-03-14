import logging
from logging.config import dictConfig
from src.common.config import LOGGING_CONFIG

dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("lab")