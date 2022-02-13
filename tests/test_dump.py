import tempfile

import properties

from . import data


def test_properties_dumps():
    assert properties.dumps(data.EXCEPT_RESULT) == data.STRING_NORMAL.strip()


def test_properties_dump():
    with tempfile.TemporaryFile("w+") as fp:
        properties.dump(data.EXCEPT_RESULT, fp)

        fp.seek(0)

        assert fp.read().strip() == data.STRING_NORMAL.strip()
