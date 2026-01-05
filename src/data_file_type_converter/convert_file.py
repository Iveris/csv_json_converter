# !/usr/bin/python3
from data_file_type_converter.csv_to_json import CsvToJson
from data_file_type_converter.json_to_csv import JsonToCsv
import sys
from argparse import ArgumentParser, Namespace

class ConvertFile:
    def __init__(self, argv: list[str]):
        self.argv: list[str] = argv
    
    def execute(self) -> int:
        try:
            args: Namespace = self._parse(self.argv)
            self._input_file = args.file
            if self._is_csv_file():
                converter: CsvToJson = CsvToJson()
            elif self._is_json_file():
                converter: JsonToCsv = JsonToCsv()
            else:
                raise ValueError("Unexpected file format. Please make sure the file ends with a csv or json suffix.")

            converter.convert(self._input_file)

            return 0
        except Exception as e:
            print(f'Exception {e}')
            return 5

    def _is_csv_file(self) -> bool:
        fileparts: list[str] = self._input_file.split('.')
        return fileparts[-1].lower() == 'csv'

    def _is_json_file(self) -> bool:
        fileparts: list[str] = self._input_file.split('.')
        return fileparts[-1].lower() == 'json'
    
    @classmethod
    def _parse(cls, argv: list[str]) -> Namespace:
        parser: ArgumentParser = ArgumentParser(prog="convert", description="concert file from csv to json")
        parser.add_argument('-f', '--file', type=str, required=True)
        return parser.parse_args(argv)

def main(argv: list[str]) -> None:
    return ConvertFile(argv).execute()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))