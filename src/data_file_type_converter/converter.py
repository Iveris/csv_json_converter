import abc

class AbstractConverter(abc.ABC):

    @abc.abstractmethod
    def convert(self, input_file: str) -> None:
        raise NotImplementedError

    def _validate_file(self, input_path: Path, output_path: Path) -> bool:
        # validate that input file exists
        if input_path.exists() == False: 
            raise FileNotFoundError(f'File {input_path} could not be found')
        # output file should not exist or there is a risk of file corruption or losing data
        if output_path.exists() == True:
            raise FileExistsError(f'Please rename or remove existing file: {output_path}')
        return True

