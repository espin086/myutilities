from setuptools import setup

setup(name='myutilities',
      version='0.1',
      description='utilities for efficiency',
      url='https://github.com/espin086/myutilities',
      author='JJ Espinoza',
      author_email='jj.espinoza.la@gmail.com',
      license='MIT',
      packages=['myutilities'],
      install_requires=[
          'twilio',
      ],
      zip_safe=False)