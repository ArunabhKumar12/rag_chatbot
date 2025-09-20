import os
from dotenv import load_dotenv

load_dotenv()

required_keys = ["OPENAI_KEY", "PINECONE_KEY", "MAX_INPUT_TOKEN", "MAX_OUTPUT_TOKEN", "MAX_DOCUMENT_SIZE"]
for key in required_keys:
    environment_var = os.getenv(key)
    if not environment_var:
        raise ValueError(f"Missing value in the Environment variable: {key}")
    else:
        print(f"Value fetched successfully for {key}")

