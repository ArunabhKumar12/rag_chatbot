from utils.logging_config import get_logger
from configs.constants import validate_env_vars

if __name__ == '__main__':
    logger = get_logger(__name__)

    logger.debug("This is a debug msg")
    logger.info("This is an info msg")
    logger.warning("This is an warning msg")
    logger.error("This is an error msg")
    logger.critical("This is an critical msg")

    env_values = validate_env_vars(logger)

    for i in range(100):
        logger.info(f"Test log message {i}")