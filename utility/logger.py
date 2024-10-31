import logging
from functools import wraps

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def logger_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        try:
            logger.info(f"Start execute {func.__name__}")
            result = func(*args, **kwargs)

            logger.info(
                f"{func.__module__}, "
                f"args:{[str(arg) for arg in args]}, "
                f"kwargs:{kwargs} Execution completed successfully.")
            return result
        except Exception as e:
            logger.error(f"An error occurred in function '{func.__name__}': {e}")
            return None

    return wrapper
