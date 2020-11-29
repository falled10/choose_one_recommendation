from environs import Env


env = Env()

env.read_env()


DATABASE_HOST = env.str('DATABASE_HOST', 'localhost')
DATABASE_PORT = env.int('DATABASE_PORT', 7687)
NEO4J_AUTH = env.str('NEO4J_AUTH')
CELERY_BROKER_URL = env.str('BROKER_URL', '')
CELERY_TASK_DEFAULT_QUEUE = env.str('CELERY_DEFAULT_QUEUE', 'fastapi')
CELERY_TASK_SOFT_TIME_LIMIT = env.int('TASK_SOFT_TIME_LIMIT_SEC', 40)
CELERY_LOG_PATH = env.path('CELERY_LOG_PATH', '.data/celery.log')
LOGS_ROTATION = '500 MB'
