#!/usr/bin/python

from setuptools import setup
import os.path

def readme():
    with open('README.rst') as f:
        return f.read()

def main():
  setup(name='pash',
      version='0.1',
      description='Run bash session from python',
      long_description=readme(),
      url='http://github.com/mimar321/Pash',
      author='Sinan Hepic',
      author_email='sinan.hepic@gmail.com',
      license='MIT',
      packages=['pash'],
      install_requires=[
          'pexpect',
      ],
      zip_safe=False,

      # Test setup
      test_suite='nose2.collector.collector',
      tests_require=['nose2'],
  )



if __name__ == "__main__":
    main()
