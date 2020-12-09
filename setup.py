# from distutils.core import setup
import os
import subprocess
from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    required = f.read().splitlines()

if 'dist' in os.listdir('.'):
    subprocess.call(["rm", "-rf", "dist/"])
if 'build' in os.listdir('.'):
    subprocess.call(["rm", "-rf", "build/"])

setup(
    name='prosemirenderer',
    version='0.0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    license='',
    author='Stefanos Liakis',
    author_email='stliakis@gmail.com',
    description='',
    install_requires=required,
    include_package_data=True,
)
