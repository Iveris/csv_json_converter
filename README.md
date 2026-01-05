# Data file converter: converts csv to json and json to csv

Simple file converter that uses the Pandas library for data conversion

## Requirements

* Python 3.14.x
* Poetry 2.x.x

### Installing Python 3.14

Python 3.14 can be installed using the official Python installer which is available at [www.python.org](https://www.python.org/downloads/release/python-3142/)

or using Homebrew:

```bash
brew install python@3.14
```

### Installing Poetry

Poetry can be installed from the command line using pip, pip3, or pipx

```bash
pipx install poetry==2.2.1
```

or using Homebrew

```bash
brew install poetry
```

### Converting Files

The first time you run the project, run the setup.sh script first to ensure the project is installed. 

Convert a csv to a json file, or a json file to a csv by running the *convert_file.sh* script located in the root directory of this project

```bash
./convert_file.sh filename.csv
```
