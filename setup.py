import pathlib
from setuptools import setup,find_packages

# Directory containing the file
FILE_LOC = pathlib.Path(__file__).parent
# Text of README
with open("README.md", "r") as fh:
    long_description = fh.read()

# Call setup()
setup(
    name = "rake_new2",
    version = "1.0.5",
    description = "A Python library that enables smooth keyword extraction from any text using the RAKE(Rapid Automatic Keyword Extraction) algorithm.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/BALaka-18/rake_new2",
    author = "Balaka Biswas",
    author_email = "balaka2605@gmail.com",
    license = "MIT",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    packages = find_packages(exclude=("tests",)),
    inlcude_package_data = True,
    install_requires = ["nltk"],
    python_requires='>=3.6',
)
