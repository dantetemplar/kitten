from pprint import pprint
from pathlib import Path
from pydantic.tools import parse_obj_as
from pydantic.dataclasses import dataclass
import json

PARSER_PATH = Path(__file__).parent
CONFIG_PATH = PARSER_PATH / "config.json"



@dataclass
class Config:
    TELEGRAM_API_TOKEN: str

    @classmethod
    def load(cls):
        with open(CONFIG_PATH) as f:
            return parse_obj_as(cls, json.load(f))
