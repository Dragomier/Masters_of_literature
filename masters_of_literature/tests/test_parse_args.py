"""
Testing functions in module parse_args.py!
"""

from masters_of_literature import parse_args
import pytest

def test_no_dictionary_given():
    with pytest.raises(SystemExit) as ext:
        parse_args.create_args(["--dictionary"])
    assert ext.value.code == 2

def test_no_work_given():
    with pytest.raises(SystemExit) as ext:
        parse_args.create_args(["--dictionary", r"masters_of_literature\dictionaries\pl.txt", "--works"])
    assert ext.value.code == 2


