import pytest
from hil.scaling import to_raw, from_raw, validate_rate


def test_to_raw_encodes_typical_rate():
    assert to_raw(123.4) == 1234

def test_int_truncation_bug():
    assert to_raw(0.7) == 7

def test_offbyoneLSB_case():
    assert to_raw(499.9) == 4999

def test_fromrawtestpytestapprox():
    assert from_raw(1234) == pytest.approx(123.4)

def test_milestoneboundaries():
    assert validate_rate(1.0) is True and validate_rate(500.0) is True

def test_stepoutsidelimit():
    assert validate_rate(0.9) is False and validate_rate(500.1) is False

def testthezeropoint1grid():
    assert validate_rate(123.45) is False

def test_negative_values():
    with pytest.raises(ValueError):
        to_raw(-1.0)

def test_encodeanddecode():
    assert from_raw(to_raw(1.0)) == pytest.approx(1.0) and from_raw(to_raw(500.0)) == pytest.approx(500.0)

def test_to_raw_accepts_full_16bit_range():
    assert to_raw(0.0) == 0
    assert to_raw(6553.5) == 65535      # 2**16 - 1 at 0.1 scale

def test_to_raw_rejects_value_one_past_16bits():
    with pytest.raises(ValueError):
        to_raw(6553.6)                   # raw 65536 doesn't fit

