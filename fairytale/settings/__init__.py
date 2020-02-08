import environ
env = environ.Env()

# reading .env file
environ.Env.read_env()

# False if not in os.environ
DEBUG = env.bool('DEBUG')

if DEBUG:
    from .development import *

    try:
        from .local import *
    except ImportError:
        pass
else:
    from .production import *
