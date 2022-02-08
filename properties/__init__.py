"""
Parser for properties file, which is a simple key-value file, comments is also supported.
"""
import io
import os
from typing import Dict, TextIO, Union

__version__ = "0.1.0"


Properties = Dict[str, str]


class BaseError(Exception):
    """Base class"""


class InvalidLineError(BaseError):
    """Invalid line"""

    def __init__(self, line_number: int, line: str):
        self.line_number = line
        self.line = line

        super().__init__(f"Invalid line {line_number}: {line}")


def loads(string: str, skip_errors: bool = False) -> Properties:
    """
    Load properties from string.

    Args:
        string: The string to load.
        skip_errors: Whether to skip invalid lines.

    Returns:
        A dictionary of properties.

    Raises:
        InvalidLineError: If skip_errors is False and an invalid line is found.
    """
    properties = dict()

    for i, line in enumerate(string.splitlines()):
        if line.startswith("#"):
            continue

        line = line.strip()
        if line:
            try:
                key, value = map(str.strip, line.split(":", 1))
            except ValueError:
                if not skip_errors:
                    raise InvalidLineError(i, line) from None
            else:
                properties[key] = value

    return properties


File = Union[str, os.PathLike, TextIO]


def _read_file(file: File) -> str:
    if isinstance(file, io.TextIOBase):
        return file.read()

    with open(str(file)) as fp:
        return fp.read()


def load(file: File, skip_errors: bool = False) -> Properties:
    """
    Load properties from file. see :func:`loads`.
    """
    return loads(_read_file(file), skip_errors)
