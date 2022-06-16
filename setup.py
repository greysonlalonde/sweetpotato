from os import path
from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="sweetpotato",
    url="https://github.com/greysonlalonde/sweetpotato",
    download_url="https://github.com/greysonlalonde/sweetpotato/v0.1.0-alpha.tar.gz",
    author="Greyson R. LaLonde",
    author_email="greyson.r.lalonde@gmail.com",
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[],
    version="v0.1.0-alpha",
    license="MIT",
    description="React-native development for python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
