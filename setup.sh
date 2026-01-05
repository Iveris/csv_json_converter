#!/bin/bash

# remove existing virtual environment if it exists
rm -rf .venv

# remove lock file to completely reset poetry installation
rm poetry.lock

# create the virtual environment in the project root rather
poetry config virtualenvs.in-project true

# install project
poetry lock
poetry install
