"""
Testing functions in module my_types.py!
"""
import pytest
from masters_of_literature.my_types import positive_int

def test_string_is_not_positive_int():
    with pytest.raises(ValueError):
        positive_int.positive_int("Ala ma kota")

def test_negative_is_not_positive_int():
    with pytest.raises(ValueError):
        positive_int.positive_int(-10)

def test_good_behavior_with_positive_int():
   assert positive_int.positive_int(10) == 10