from pathlib import Path
from pydantic.tools import parse_obj_as
from pydantic.dataclasses import dataclass
import json

PARSER_PATH = Path(__file__).parent
CONFIG_PATH = PARSER_PATH / "config.json"
TOKEN_PATH = PARSER_PATH / "token.json"

# if not token.json exists, create it
if not TOKEN_PATH.exists():
    with open(TOKEN_PATH, "w") as f:
        token = input("Enter your telegram api token: ")
        json.dump({"token": token}, f)


@dataclass
class Config:
    TELEGRAM_API_TOKEN: str = json.load(open(TOKEN_PATH))["token"]

    def update_token(self, token: str):
        with open(TOKEN_PATH, "w") as f:
            json.dump({"token": token}, f)
        self.TELEGRAM_API_TOKEN = token

    @classmethod
    def load(cls):
        with open(CONFIG_PATH) as f:
            return parse_obj_as(cls, json.load(f))


CONFIG = Config.load()

__all__ = ["CONFIG", "PARSER_PATH"]

if __name__ == '__main__':
    print(CONFIG)
