from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from _typeshed import SupportsRead, SupportsWrite


__version__ = "0.3.0"


Properties = Dict[str, str]


class BaseError(Exception):
    pass


class InvalidLineError(BaseError):
    def __init__(self, line_number: int, line: str):
        self.line_number = line_number
        self.line = line

        super().__init__(f"Invalid line {line_number}: {line}")


def loads(string: str, skip_errors: bool = False) -> Properties:
    properties = dict()

    for i, line in enumerate(string.splitlines(), start=1):
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


def load(fp: "SupportsRead[str]", skip_errors: bool = False) -> Properties:
    return loads(fp.read(), skip_errors)


def dumps(properties: Properties) -> str:
    lines = []
    for key, value in properties.items():
        lines.append(f"{key}: {value}")
    return "\n".join(lines)


def dump(properties: Properties, fp: "SupportsWrite[str]") -> None:
    fp.write(dumps(properties))
