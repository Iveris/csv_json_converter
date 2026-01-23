from data_file_type_converter.json_to_csv import JsonToCsv
import json
import os
from pathlib import Path
import pandas as pd

TEST_FILE_INPUT: str = "tests/test_data/test_data.json"
TEST_FILE_OUTPUT: str = "tests/test_data/test_data.json.csv"

def test_convert_givenCsvFile_returnsJson():
    # arrange
    converter: JsonToCsv = JsonToCsv()
    # act
    converter.convert(input=TEST_FILE_INPUT)
    # assert
    input_data = pd.read_json(TEST_FILE_INPUT, orient='records', precise_float=True)
    with open(TEST_FILE_OUTPUT, "r", encoding="utf-8") as file:
        headers: List[str] = file.readline().split(',')
        for row in input_data.itertuples():
            line: List[str] = file.readline().split(',')
            for i in range(0, len(headers)):
                assert str(line[i]).strip() == str(row[i + 1]).strip()

    # cleanup
    file.close()
    output_path: Path = Path(TEST_FILE_OUTPUT)
    os.remove(output_path)
