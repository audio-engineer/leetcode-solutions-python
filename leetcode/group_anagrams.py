"""49. Group Anagrams.

https://leetcode.com/problems/group-anagrams/description/
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: dict[str, list[str]] = {}

        for str_ in strs:
            s = "".join(sorted(str_))

            if s in anagrams:
                anagrams[s].append(str_)
            else:
                anagrams[s] = [str_]

        return list(anagrams.values())
