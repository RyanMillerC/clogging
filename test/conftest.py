import pytest

import utils


@pytest.fixture
def requires_tmp():
    """Create tmp directory if it doesn't exist already. ``tmp``
    is used in several file logging tests.
    """
    utils.create_dirs('test/tmp')
