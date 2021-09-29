from setuptools import setup, find_packages
from setuptools.command.install import install
from os import path
import subprocess

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # $ pip install stainaug
    name='stainaug',
    version='0.0.2',
    description='A tool for H&E image augmentation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/estorrs/stainaug',
    author='Erik Storrs',
    author_email='estorrs@gmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='H&E stain augmentation',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'matplotlib',
        'numpy',
        'Pillow',
        'scikit-image',
        'scipy'
        ],
    include_package_data=True,
)
