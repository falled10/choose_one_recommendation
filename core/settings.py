from environs import Env


env = Env()

env.read_env()


DATABASE_HOST = env.str('DATABASE_HOST', 'localhost')
DATABASE_PORT = env.int('DATABASE_PORT', 7687)
NEO4J_AUTH = env.str('NEO4J_AUTH')
