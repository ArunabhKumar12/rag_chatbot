import os
from dotenv import load_dotenv

# Logging constants

LOG_LEVEL = "DEBUG"
LOG_FILE = "logs/app.log"
MAX_BYTES = 5*1024*1024
BACKUP_COUNT = 5

# Environment variables

load_dotenv()
required_keys = ["OPENAI_KEY", "PINECONE_KEY", "MAX_INPUT_TOKEN", "MAX_OUTPUT_TOKEN", "MAX_DOCUMENT_SIZE"]
def validate_env_vars(logger) -> dict[str, str]:
    env_values = {}
    # loading environment variables
    for key in required_keys:
        environment_var = os.getenv(key)
        if not environment_var:
            logger.error(f"Missing value in the Environment variable: {key}")
            raise ValueError(f"Missing value in the Environment variable: {key}")
        else:
            logger.info(f"Value fetched successfully for {key}")
            env_values[key] = environment_var
    return env_values