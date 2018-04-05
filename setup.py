import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='abacus-tpot',
      packages=['abacus_tpot'],
      version='0.9',
      description="TPOT's analysis library",
      long_description=read('README.rst'),
      keywords=['analysis', 'data', 'tpot', 'library'],
      url='https://github.com/workforce-data-initiative/abacus-tpot',
      download_url='https://github.com/workforce-data-initiative/abacus-tpot/archive/0.9.tar.gz',
      author='Stanley Ndagi, Tom Plagge',
      author_email='stanley@brighthive.io, tom@brighthive.io',
      license='Apache 2.0',
      zip_safe=True)
