import json
from datetime import datetime
from typing import Any, Dict


def load_config(filepath: str) -> Dict[str, Any]:
    """
    Load config from json file.

    Parameters:
        filepath (str): Path to json file

    Returns:
        data (Dict[str, Any]): Config as a dictionary
    """
    with open(filepath) as file:
        data: Dict[str, Any] = json.load(file)
    return data


def print_system_msg(msg: str) -> None:
    """
    Print a message to the terminal.

    Parameters:
        msg (str): Message to print
    """
    print(f"[{datetime.now().strftime('%d-%m-%G | %H:%M:%S')}] {msg}")
