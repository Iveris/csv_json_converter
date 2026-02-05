import pandas as pd
from pathlib import Path
from data_file_type_converter.converter import AbstractConverter

class JsonToCsv(AbstractConverter):

    FILE_TYPE: str = 'csv'

    # By default, the output path will match the input file except for the suffix.
    # This clearly identifies the files contain the same data, but in different formats
    def _create_default_file_paths(self, file_path: str) -> (Path, Path):
        input: Path = Path(file_path)
        output: str = '.'.join((file_path, self.FILE_TYPE))
        return input, Path(output)
    
    def convert(self, input: str):
        input_file, output_file = self._create_default_file_paths(input)
        is_valid: bool = self._validate_file(input_file, output_file)
        dataframe = pd.read_json(input_file, orient='records', precise_float=True)
        dataframe.to_csv(output_file, float_format="%.5f", index=False)
        # comment out the line above and uncomment the line below to add an index to each entry
        # dataframe.to_csv(output_file, float_format="%.2f", index_label="index")
        