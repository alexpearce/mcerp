"""Define mcerp version and author.

This is not defined in __init__ as that file imports dependencies of mcerp.
Before mcerp is installed, when those dependencies may not be present,
we might need to access mcerp metadata. It can be accessed by importing this
file, for example `from mcerp._version import __version__`.
"""
__version_info__ = (0, 11)
__version__ = '.'.join(map(str, __version_info__))

__author__ = 'Abraham Lee'
