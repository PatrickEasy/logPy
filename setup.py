from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="logpy-utils",
    version="0.1.0",
    author="PatrickEasy",
    description="Simple set of Python scripts to automatically create, record and delete message logs from python scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PatrickEasy/logPy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
