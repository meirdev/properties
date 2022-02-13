import pytest

import properties

from . import data


def test_properties_loads():
    assert properties.loads(data.STRING_NORMAL) == data.EXCEPT_RESULT


def test_properties_loads_comments():
    assert properties.loads(data.STRING_COMMENTS) == data.EXCEPT_RESULT


def test_properties_loads_invalid_line():
    with pytest.raises(properties.InvalidLineError) as error:
        properties.loads(data.STRING_INVALID_LINE)

    assert error.value.line == "invalid line"
    assert error.value.line_number == 3


def test_properties_loads_skip_errors():
    assert (
        properties.loads(data.STRING_INVALID_LINE, skip_errors=True)
        == data.EXCEPT_RESULT
    )


def test_properties_load_file_pointer():
    with open(data.FILE_PATH, "r") as fp:
        assert properties.load(fp) == data.EXCEPT_RESULT
