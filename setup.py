from setuptools import setup

def readme():
    with open('README.rst') as readme_file:
        return readme_file.read()

setup(name="Robber language",
      version='0.1',
      description='Robber language encoding/decoding using Codecs library',
      long_description=readme(),
      packages='robberlanguage',
      zip_safe=False
)
