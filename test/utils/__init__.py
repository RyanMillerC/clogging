"""Helper utils for pytest tests
"""

import logging
import os

from six import string_types


def cleanup(*args):
    """Cleanup Logger instances and delete tmp files. Pass
    in any number of both Logger instances and str paths
    to tmp files to be removed.

    NOTE: Better to stick Logger instances first in order.
    Otherwise, files could be in use and will throw OS error.
    """
    for obj in args:
        if isinstance(obj, logging.Logger):
            # Remove Logger instance handlers
            obj.handlers = []
        if isinstance(obj, string_types):
            # Object is str - so it is a path to a file
            if os.path.exists(obj):
                os.remove(obj)


def create_dirs(*args):
    """Create directories from arguement strs. Uses makedirs
    so parent directories will be automatically created for
    nested children.
    """
    for dir_ in args:
        if not os.path.exists(dir_):
            os.makedirs(dir_)
