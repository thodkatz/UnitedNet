from distutils.core import setup
from setuptools import find_namespace_packages

setup(
    name='UnitedNet',
    version="0.1.0",
    packages=find_namespace_packages(exclude=["tests"]),
    url='',
    license='',
    author='thodkatz',
    author_email='',
    description='',
    install_requires=[
        "matplotlib",
        "ipykernel",
        "scanpy",
        "numpy",
        "pandas",
        "torch",
        "tabulate",
        "scikit-learn",
        "shap",
        "mne-connectivity"
        ]
)
