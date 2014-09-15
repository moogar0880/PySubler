"""Utilities for assisting with the writing/tagging of metadata"""
import sys
import subprocess

__all__ = ['subler_executable']


def subler_executable():
    """Find a localized subler executable and return it's path. If no executable
    can be found, None is returned
    """
    try:
        executable = subprocess.check_output('which SublerCLI',
                                             shell=True).strip()
    except subprocess.CalledProcessError:
        return ''
    if sys.version_info[0] == 3:
        executable = executable.decode('UTF-8')
    if executable == '':
        return 'SublerCLI'
    return executable
