# Config Module

## Overview

This Python module reads configuration files in `.yaml`, `.cfg`, and `.conf` formats, flattens them, and provides functionality to write configurations to `.env` and `.json` files or set environment variables.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd config_module
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

```python
from config_module.env_manager import ConfigManager

# Create a ConfigManager instance with the path to your configuration file
manager = ConfigManager('path/to/config.yaml')

# Write configurations to a JSON file
manager.write_to_json('path/to/config.json')

# Write configurations to an ENV file
manager.write_to_env('path/to/config.env')

# Set configurations as environment variables
manager.set_environment()
