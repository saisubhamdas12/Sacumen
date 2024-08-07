import json
import os
from typing import Dict, Any

def write_json(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def write_env(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as file:
        for key, value in data.items():
            file.write(f'{key}={value}\n')

def set_env_variables(data: Dict[str, Any]) -> None:
    for key, value in data.items():
        os.environ[key] = value
