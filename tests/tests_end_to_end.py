import os
from pathlib import Path

import pytest
from click.testing import CliRunner

import plyg


@pytest.mark.unadded_feature
def test_that_calling_plyg_bus_creates_a_messagebus_and_test_file():
    # GIVEN
    test_runner = CliRunner()

    # WHEN calling plyg bus
    result = test_runner.invoke(plyg.cli, ['bus'])

    # THEN the files are generated
    assert os.path.isfile(Path('messagebus.py'))
    assert os.path.isfile(Path('test_messagebus.py'))
    assert result.output == 'Beep Beep Bus is here to take you to the events by your command!'

    # THEN the the files are as expected
    with open(Path('messagebus.py')) as fh:
        contents = fh.read()
        assert contents == """This is not completed"""

