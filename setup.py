import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="column",
    version="1.0",
    author="Dishit Pala",
    author_email="dishitpala@gmail.com",
    description="A python library for fetching, cleaning & sorting the CSV file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dishitpala/column",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)