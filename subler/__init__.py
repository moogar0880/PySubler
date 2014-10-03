"""This module provides an easily scriptable interface to tagging x264 video
format metadata via the SublerCLI.
"""

from .subler import *
from . import tools

version_info = (0, 4, 1)

__author__ = 'Jon Nappi'
__version__ = '.'.join([str(x) for x in version_info])
