from data_file_type_converter.csv_to_json import CsvToJson
import json
import os
from pathlib import Path

TEST_FILE_INPUT: str = "tests/test_data/test_data.csv"
TEST_FILE_OUTPUT: str = "tests/test_data/test_data.csv.json"

def test_convert_givenCsvFile_returnsJson():
    # arrange
    converter: CsvToJson = CsvToJson()
    # act
    converter.convert(input=TEST_FILE_INPUT)
    # assert
    with open(TEST_FILE_OUTPUT, "r", encoding="utf-8") as file:
        def keep_reading(line:str) -> bool:
            return not (line or line.startswith("]"))

        line: str = file.readline()

        while keep_reading(line):
            if line.startswith("["):
                continue
            json_object: dict = json.loads(clean_line(line))
            assert json_object['id'] is not None
            line = file.readline()
    # cleanup
    file.close()
    output_path: Path = Path(TEST_FILE_OUTPUT)
    os.remove(output_path)
