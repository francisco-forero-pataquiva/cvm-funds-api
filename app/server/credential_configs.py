import dotenv
import os
from pathlib import Path


def access_configuration():
    dotenv_file = dotenv.find_dotenv()
    if dotenv_file == "":
        Path('./.env').touch()
        dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)

    if os.environ.get("DB_USER") is None:
        print("Please fill in the requested credentials:")
        os.environ["DB_USER"] = input("Enter your database username:")
        dotenv.set_key(dotenv_file, "DB_USER", os.environ["DB_USER"])
        os.environ["DB_PASSWORD"] = input("Enter your database password: ")
        dotenv.set_key(dotenv_file, "DB_PASSWORD", os.environ["DB_PASSWORD"])
        