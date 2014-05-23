from setuptools import setup

setup(
    name='mite',
    version='0.1.0',
    author='Samuel "mansam" Lucidi',
    author_email="mansam@csh.rit.edu",
    packages=['mite'],
    url='http://pypi.python.org/pypi/validator.py/',
    license='LICENSE',
    install_requires=['webob'],
    tests_require=['pytest', 'validator.py'],
    test_suite="tests",
    description='A tiny WSGI framework.',
    long_description=open('README.rst').read()
)
