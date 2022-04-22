#!/usr/bin/env python3
"""
Type-annotated function sum_mixed_list
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Type-annotated function sum_mixed_list
    """
    return [(i, len(i)) for i in lst]
