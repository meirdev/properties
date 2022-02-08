import pytest

import properties
from . import data


def test_version():
    assert properties.__version__ == "0.1.0"


def test_properties_loads():
    assert properties.loads(data.STRING_NORMAL) == data.EXCEPT_RESULT


def test_properties_loads_comments():
    assert properties.loads(data.STRING_COMMENTS) == data.EXCEPT_RESULT


def test_properties_loads_invalid_line():
    with pytest.raises(properties.InvalidLineError):
        properties.loads(data.STRING_INVALID_LINE)


def test_properties_loads_skip_errors():
    assert (
        properties.loads(data.STRING_INVALID_LINE, skip_errors=True)
        == data.EXCEPT_RESULT
    )


def test_properties_load_file_pointer():
    with open(data.FILE_PATH, "r") as fp:
        assert properties.load(fp) == data.EXCEPT_RESULT


def test_properties_load_file_path():
    assert properties.load(data.FILE_PATH) == data.EXCEPT_RESULT
