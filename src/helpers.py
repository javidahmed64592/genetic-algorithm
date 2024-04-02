import json
from datetime import datetime
from typing import Any, Dict


def load_config(filepath: str) -> Dict[str, Any]:
    with open(filepath) as file:
        data: Dict[str, Any] = json.load(file)
    return data


def print_system_msg(msg: str) -> None:
    print(f"[{datetime.now().strftime('%d-%m-%G | %H:%M:%S')}] {msg}")
