import io
import os
import re

from setuptools import find_packages, setup  # type: ignore


def read(path):
    path = os.path.join(os.path.dirname(__file__), path)
    with io.open(path, "r", encoding="utf-8") as f:
        return f.read()


setup(
    name="tratai",
    version="0.1.0",
    description="A tiny tool for pomodoros",
    long_description=read("README.rst"),
    platforms=["any"],
    packages=["src"],
    namespace_packages=["src"],
    entry_points={"console_scripts": ["tratai = src.main:main"]},
    install_requires=["rich==3.3.2", "click==7.1.2"],
    extras_require={
        "test": ["black==18.9b0", "flake8==3.7.7", "mypy==0.782", "isort==5.4.2"]
    },
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)
