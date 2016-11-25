from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

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
      zip_safe=False)

