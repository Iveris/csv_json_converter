#!/bin/bash

OG_DIR=$(pwd)
SCRIPT_DIR=$(dirname "$0")
cd $SCRIPT_DIR

# Uncomment the line below to reset poetry installation for this project
#./setup.sh

poetry run python src/data_file_type_converter/convert_file.py -f "$1"

cd $OG_DIR
