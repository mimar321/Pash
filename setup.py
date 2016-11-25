from setuptools import setup

setup(name='pash',
      version='0.1',
      description='Run bash session from python',
      url='http://github.com/mimar321/Pash',
      author='Sinan Hepic',
      author_email='sinan.hepic@gmail.com',
      license='MIT',
      packages=['pash'],
      install_requires=[
          'pexpect',
      ],
      zip_safe=False)

