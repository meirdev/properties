from setuptools import setup, find_packages

from properties import __version__

URL = "https://github.com/meirdev/properties"
PYTHON_REQUIRES = ">=3.7"

setup(
    name="properties",
    url=URL,
    python_requires=PYTHON_REQUIRES,
    version=__version__,
    packages=find_packages(),
    entry_points={"console_scripts": ["properties = properties.__main__:main"]},
)
