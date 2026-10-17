"""Conversion between engineering values and raw CAN signal integers.

The rate signal in PUMP_STATUS (0x100) and PUMP_CMD (0x200) is an unsigned
16-bit integer in units of 0.1 mL/h (SRS-002).
"""
import math

RATE_SCALE = 0.1   # mL/h per raw count
RATE_MIN = 1.0     # mL/h (SRS-002)
RATE_MAX = 500.0   # mL/h (SRS-002)


def to_raw(value: float, *, scale: float = RATE_SCALE, offset: float = 0.0, bits: int = 16) -> int:
    """Encode a physical value as a raw unsigned integer: raw = round((value - offset) / scale).

    Raises ValueError if the result does not fit in an unsigned field of `bits` bits.
    """
    raw = round((value - offset) / scale)
    if 0 < raw <= (2**bits -1):
        pass
    else:
        raise ValueError(f"{raw} does not fit in an unsigned field of {bits} bits")
    return raw

def from_raw(raw: int, *, scale: float = RATE_SCALE, offset: float = 0.0) -> float:
    """Decode a raw integer to a physical value: value = raw * scale + offset."""
    value = raw * scale + offset
    return value

def validate_rate(rate: float) -> bool:
    """True if rate is within RATE_MIN..RATE_MAX (inclusive) and on the 0.1 mL/h grid."""
    return RATE_MIN <= rate <= RATE_MAX and math.isclose(rate*10,round(rate*10))
