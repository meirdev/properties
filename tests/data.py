from pathlib import Path

BASE_DIR = Path(__file__).parent

FILE_PATH = BASE_DIR / "example.txt"

STRING_NORMAL = """
FULL NAME: John Doe
AGE: 42
TIME: 12:00
"""

STRING_COMMENTS = """
# This is a comment
FULL NAME: John Doe
AGE: 42
# This is another comment
TIME: 12:00
"""

STRING_INVALID_LINE = """
FULL NAME: John Doe
invalid line
AGE: 42
TIME: 12:00
"""

EXCEPT_RESULT = {
    "FULL NAME": "John Doe",
    "AGE": "42",
    "TIME": "12:00",
}
