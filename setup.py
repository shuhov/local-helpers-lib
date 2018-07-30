from setuptools import setup, find_packages


__author__ = "Shuhov Ivan"
__version__ = "0.0.1"

setup(
    name="local-helpers-lib",
    version=__version__,
    packages=find_packages(),
    install_requires=[],
    author=__author__,
    description="This library makes local development simpler",
    project_urls={
        "Source Code": "https://github.com/shuhov/local-helpers-lib",
    }
)