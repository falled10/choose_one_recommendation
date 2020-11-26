from loguru import logger

from core.settings import CELERY_LOG_PATH, LOGS_ROTATION


CELERY_LOGGER_NAME = 'celery_logger'


logger.add(CELERY_LOG_PATH, format="{time} {level} {message}", rotation=LOGS_ROTATION,
           filter=lambda record: record["extra"].get("name") == CELERY_LOGGER_NAME)

celery_logger = logger.bind(name=CELERY_LOGGER_NAME)
