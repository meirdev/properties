from setuptools import setup, find_packages

from properties import __version__

setup(
    name="properties",
    version=__version__,
    packages=find_packages(),
    entry_points={"console_scripts": ["properties = properties.__main__:main"]},
)
