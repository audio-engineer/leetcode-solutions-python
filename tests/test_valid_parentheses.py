"""20. Valid Parentheses.

https://leetcode.com/problems/valid-parentheses/description/
"""

import pytest

from leetcode.valid_parentheses import Solution


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("]", False),
    ],
)
def test_is_valid(s: str, expected: int) -> None:
    assert expected == Solution().isValid(s)
