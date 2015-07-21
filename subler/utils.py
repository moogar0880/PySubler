# -*- coding: utf-8 -*-
"""Utilities for assisting with the writing/tagging of metadata"""
import sys
import logging
import subprocess

__all__ = ['subler_executable', 'get_output']


def subler_executable():
    """Find a localized subler executable and return it's path. If no
    executable can be found, None is returned
    """
    try:
        executable = subprocess.check_output(['which', 'SublerCLI']).strip()
    except subprocess.CalledProcessError:
        logging.warning('Unable to find SublerCLI executable. Please ensure '
                        'that it is available in the current $PATH.')
        return ''
    if sys.version_info[0] == 3:
        executable = executable.decode('UTF-8')
    if executable == '':
        return 'SublerCLI'
    return executable


def get_output(input_args):
    """Pass the provided *input_args* ``list`` to `subprocess.check_output`.
    The decoded and stipped output is then returned

    :param input_args: Parameters to pass to the `*popenargs` argument of the
        `subprocess.check_output` function call
    :return: The decoded and stripped return value of the call to
        `subprocess.check_output`
    """
    logging.debug('get_output running with %s', str(input_args))
    output = subprocess.check_output(input_args)
    logging.debug('Command Output: %s', output)
    if sys.version_info[0] == 3:
        return output.decode('UTF-8').strip()
    else:
        return output.strip()
