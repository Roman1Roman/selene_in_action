from pathlib import Path

import tests


def path_file(file_name) -> str:
    return str(
        Path(tests.__file__).parent.joinpath(f'files/{file_name}')
    )