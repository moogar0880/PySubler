#!/usr/bin/env python
from __future__ import print_function
import sys
import shutil
import zipfile
import subprocess

if sys.version_info[0] == 2:
    from urllib2 import urlopen
elif sys.version_info[0] == 3:
    from urllib.request import urlopen

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


def install_subler():
    """Check to see if we need the SublerCLI Binary, and if so, download and
    install it to /usr/bin/env/SublerCLI"""
    url = 'https://subler.googlecode.com/files/SublerCLI-0.19.zip'
    zip_file = 'SublerCLI-0.19.zip'
    binary = 'SublerCLI'
    try:
        path = subprocess.check_output('which SublerCLI', shell=True)
        print('SublerCLI found at {}'.format(path.strip()))
    except subprocess.CalledProcessError as ex:
        path = ''
        print('No SublerCLI found.')

    if path.strip() == '':
        # We know SublerCLI isn't installed or isn't on the user's path
        with open(zip_file, 'wb') as f:
            print('Downloading SublerCLI...')
            content = urlopen(url).read()
            f.write(content)

        # Extract binary to SublerCLI
        print('Extracting SublerCLI binary...')
        zipfile.ZipFile(zip_file).extractall(binary)

        # Move SublerCLI binary into /usr/local/bin
        print('Moving SublerCLI into place...')
        shutil.move('{}/{}'.format(binary, binary), '/usr/local/bin/SublerCLI')

install_subler()


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
