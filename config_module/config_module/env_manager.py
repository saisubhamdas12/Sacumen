from .config_reader import read_config
from .config_writer import write_json, write_env, set_env_variables

class ConfigManager:
    def __init__(self, file_path: str):
        self.config = read_config(file_path)
    
    def write_to_json(self, file_path: str) -> None:
        write_json(file_path, self.config)
    
    def write_to_env(self, file_path: str) -> None:
        write_env(file_path, self.config)
    
    def set_environment(self) -> None:
        set_env_variables(self.config)
