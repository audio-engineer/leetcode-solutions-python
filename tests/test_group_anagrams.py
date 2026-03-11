"""49. Group Anagrams.

https://leetcode.com/problems/group-anagrams/description/
"""

from typing import List

import pytest

from leetcode.group_anagrams import Solution


@pytest.mark.parametrize(
    ("strs", "expected"),
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_group_anagrams(strs: List[str], expected: list[list[str]]) -> None:
    assert expected == Solution().groupAnagrams(strs)
