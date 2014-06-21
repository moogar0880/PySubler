"""This module provides an easily scriptable interface to tagging x264 video
format metadata via the SublerCLI.
"""

from .subler import *

version_info = (0, 2, 0)

__author__ = 'Jon Nappi'
__version__ = '.'.join([str(x) for x in version_info])
