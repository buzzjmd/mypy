#from distutils.core import setup
from setuptools import setup, find_packages

setup(name='mypy',
      version='0.1.0',
      description='My Python Library',
      author='buzzjmd',
      author_email='buzzjmd@gmail.com',
      packages=find_packages(where='src'),
      package_dir={'': 'src'},      
     )
