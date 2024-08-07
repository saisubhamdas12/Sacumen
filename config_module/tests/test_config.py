import pytest
import json
import os
import yaml
from config_module.config_reader import read_config, flatten_dict
from config_module.config_writer import write_json, write_env, set_env_variables
from config_module.env_manager import ConfigManager

@pytest.fixture
def sample_data():
    return {
        'key1': 'value1',
        'key2': 'value2',
        'nested': {
            'key3': 'value3',
            'nested2': {
                'key4': 'value4'
            }
        }
    }

def test_flatten_dict(sample_data):
    flat_data = flatten_dict(sample_data)
    expected = {
        'key1': 'value1',
        'key2': 'value2',
        'nested.key3': 'value3',
        'nested.nested2.key4': 'value4'
    }
    assert flat_data == expected

def test_read_config_yaml(sample_data):
    with open('test.yaml', 'w') as file:
        yaml.dump(sample_data, file)
    assert read_config('test.yaml') == flatten_dict(sample_data)

def test_write_json(sample_data):
    flat_data = flatten_dict(sample_data)
    write_json('test.json', flat_data)
    with open('test.json', 'r') as file:
        assert json.load(file) == flat_data

def test_write_env(sample_data):
    flat_data = flatten_dict(sample_data)
    write_env('test.env', flat_data)
    with open('test.env', 'r') as file:
        lines = file.readlines()
        assert lines[0].strip() == 'key1=value1'
        assert lines[1].strip() == 'key2=value2'
        assert lines[2].strip() == 'nested.key3=value3'
        assert lines[3].strip() == 'nested.nested2.key4=value4'

def test_set_environment(sample_data):
    flat_data = flatten_dict(sample_data)
    set_env_variables(flat_data)
    assert os.environ['key1'] == 'value1'
    assert os.environ['key2'] == 'value2'
    assert os.environ['nested.key3'] == 'value3'
    assert os.environ['nested.nested2.key4'] == 'value4'

def test_config_manager(sample_data):
    with open('test.yaml', 'w') as file:
        yaml.dump(sample_data, file)
    
    manager = ConfigManager('test.yaml')
    manager.write_to_json('test.json')
    manager.write_to_env('test.env')
    manager.set_environment()

    with open('test.json', 'r') as file:
        assert json.load(file) == flatten_dict(sample_data)

    with open('test.env', 'r') as file:
        lines = file.readlines()
        assert lines[0].strip() == 'key1=value1'
        assert lines[1].strip() == 'key2=value2'
        assert lines[2].strip() == 'nested.key3=value3'
        assert lines[3].strip() == 'nested.nested2.key4=value4'

    assert os.environ['key1'] == 'value1'
    assert os.environ['key2'] == 'value2'
    assert os.environ['nested.key3'] == 'value3'
    assert os.environ['nested.nested2.key4'] == 'value4'
