import yaml
import configparser
from typing import Dict, Any

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

def read_yaml(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return flatten_dict(data)

def read_cfg(file_path: str) -> Dict[str, Any]:
    config = configparser.ConfigParser()
    config.read(file_path)
    data = {section: dict(config.items(section)) for section in config.sections()}
    return flatten_dict(data)

def read_conf(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        data = dict(line.strip().split('=', 1) for line in file if '=' in line)
    return flatten_dict(data)

def read_config(file_path: str) -> Dict[str, Any]:
    if file_path.endswith('.yaml'):
        return read_yaml(file_path)
    elif file_path.endswith('.cfg'):
        return read_cfg(file_path)
    elif file_path.endswith('.conf'):
        return read_conf(file_path)
    else:
        raise ValueError("Unsupported file format")
