from os import path

from setuptools import find_packages, setup

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "README.md")) as f:
    README = f.read()

setup(
    name="tia-openness-api-client",
    packages=find_packages(),
    version="0.0.1",
    description="TIA Openness API Client",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Jasper Delahaije",
    author_email="jdelahaije@gmail.com",
    license="MIT",
    python_requires=">=3.11",
    requires=[],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Natural Language :: English",
        "Natural Language :: Dutch",
    ],
)