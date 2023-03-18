import os
from pathlib import Path
from pydantic.tools import parse_obj_as
from pydantic import BaseModel, validator, root_validator
import json

PARSER_PATH = Path(__file__).parent
CONFIG_PATH = PARSER_PATH / "config.json"


class Settings(BaseModel):
    """ Settings for the program.
    You can set it in config.json or in ENV variables(for sensitive data).
    All field names are case-insensitive(converted to uppercase).
    """
    VERSION: str
    TITLE: str
    TELEGRAM_API_TOKEN: str = None

    @validator('TELEGRAM_API_TOKEN', pre=True, always=True)
    def check_telegram_api_token(cls, v):
        if v is None:
            # get token from ENV variables
            v = os.getenv('TELEGRAM_API_TOKEN', None)
            if v is None:
                # get token from user input
                v = input(
                    "Enter your telegram api token"
                    "(or you can set it in ENV variables and restart the "
                    "program):"
                )
        return v

    @root_validator(pre=True)
    def keys_to_upper(cls, values):
        # convert all keys to upper case
        return {k.upper(): v for k, v in values.items()}


def load_config(config_path: Path = CONFIG_PATH):
    with open(config_path) as f:
        data = json.load(f)
    return parse_obj_as(Settings, data)


SETTINGS = load_config()

__all__ = ["SETTINGS", "PARSER_PATH"]

if __name__ == '__main__':
    print(SETTINGS)
