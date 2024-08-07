# setup.py

from setuptools import setup, find_packages

setup(
    name='config_module',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'configparser',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'config_module=config_module.config:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A module to read various configuration file formats and convert them to a flat dictionary.',
    keywords='config parser yaml cfg conf json env',
)
