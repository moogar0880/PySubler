#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    import subler
except ImportError:
    pass

packages = ['subler']
requires = []

with open('README.rst') as f:
    readme = f.read()

setup(
    name='subler',
    version=subler.__version__,
    description='Python interface to the Subler style metadata tagging.',
    long_description=readme,
    author='Jonathan Nappi',
    author_email='moogar@comcast.net',
    url='https://github.com/moogar0880/PySubler',
    packages=packages,
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',

    ),
)
