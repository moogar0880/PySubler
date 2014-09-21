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

with open('README.rst') as f:
    readme = f.read()
with open('HISTORY.rst') as f:
    history = f.read()

setup(
    name='subler',
    version=subler.__version__,
    description='Python interface to the Subler style metadata tagging.',
    long_description='\n\n'.join([readme, history]),
    author='Jonathan Nappi',
    author_email='moogar@comcast.net',
    url='https://github.com/moogar0880/PySubler',
    packages=packages,
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['pysubler = subler.cli:main']
    },
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Environment :: MacOS X',
        'Operating System :: MacOS :: MacOS X',
    ),
)
