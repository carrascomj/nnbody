"""Setup file for packaging."""
from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="nnbody",
    version="0.1.0",
    description="NNETS lundbeck antibodies",
    author="Jorge Carrasco Muriel",
    author_email="jocc@lundbeck.com",
    keywords="python metabolic-models bioinformatics antibodies",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "sklearn",
        "torch",
        "torchvision",
        "matplotlib",
    ],
    zip_safe=False,
)
