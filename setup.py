from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

description = "Simple Docker container orchestration tool"
long_description = open("README.md").read()
url = "https://github.com/JoyoDev/koden"


setup(
    name="koden",
    version="0.0.1",
    author="Aleksandar Milanovic",
    author_email="joyo.development@gmail.com",
    description=description,
    license="MIT",
    keywords="docker container orchestration",
    url=url,
    packages=find_packages(),
    long_description=long_description,
    classifiers=[],
)
