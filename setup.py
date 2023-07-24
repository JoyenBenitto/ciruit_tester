"""The setup script."""

import os
from setuptools import setup, find_packages
import codecs

# Base directory of package
here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()
def read_requires():
    with open(os.path.join(here, "arduino_tester/requirements.txt"),
              "r") as reqfile:
        return reqfile.read().splitlines()

with open("README.md", "r") as fh:
    readme = fh.read()


setup(
    name='ALUator',
    version='0.1.0',
    description="Arduino circuit tester",
    long_description= readme + '\n\n',
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: MIT",
        "Development Status :: Beta"
    ],
    keywords = "ant_gen",
    url = 'https://github.com/JoyenBenitto/ALUator',
    author = "Joyen Benitto",
    author_email = 'joyen.benitto12@gmail.com',
    license = "BSD 2-Clause License",
    packages = find_packages(),
    install_requires = ["requests"],
    python_requires = ">=3.10",
    entry_points={
        'console_scripts': ['arduino_tester=arduino_tester.main:cli'],
    },
    include_package_data=True,
    tests_require=[],
    zip_safe=False
)