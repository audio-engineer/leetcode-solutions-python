"""242. Valid Anagram.

https://leetcode.com/problems/valid-anagram/description/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = [0] * 26
        freq_t = [0] * 26

        ascii_a = ord("a")

        if len(s) != len(t):
            return False

        for i, _ in enumerate(s):
            freq_s[ord(s[i]) - ascii_a] += 1
            freq_t[ord(t[i]) - ascii_a] += 1

        return freq_s == freq_t
