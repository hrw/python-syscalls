#!/usr/bin/python3

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="system-calls",
    version="5.13.0",
    author="Marcin Juszkiewicz",
    author_email="marcin-python@juszkiewicz.com.pl",
    description="Python module to check for system call numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hrw/python-syscalls",
    project_urls={
        "Bug Tracker": "https://github.com/hrw/python-syscalls/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    packages=["syscalls", "syscalls/tables/"],
    python_requires=">=3.6",
    license_files=["LICENSE"],
)
