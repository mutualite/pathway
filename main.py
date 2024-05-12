import importlib
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":

    apikey = os.environ.get('GEMINI_API_TOKEN')
    if apikey == "":
        raise Exception("The environment variable 'GEMINI_API_TOKEN' is not set.")

    host = os.environ.get("HOST", "api")
    port = int(os.environ.get("PORT", 8080))
    app_api = importlib.import_module("api.api")
    app_api.run(host=host, port=port)
