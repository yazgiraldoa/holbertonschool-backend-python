#!/usr/bin/env python3
"""
Type-annotated function sum_mixed_list
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Type-annotated function to_kv that takes a string k and an int
    OR float v as arguments and returns a tuple.
    """
    return lambda x: x * multiplier
