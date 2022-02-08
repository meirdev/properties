import json
import sys
import unittest.mock

from properties.__main__ import main
from . import data


def test_main(capsys):
    with unittest.mock.patch.object(sys, "argv", ["", str(data.FILE_PATH)]):
        main()
        captured = capsys.readouterr()
        assert json.loads(captured.out) == data.EXCEPT_RESULT
