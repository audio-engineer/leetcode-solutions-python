"""3. Longest Substring Without Repeating Characters.

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen: set[str] = set()
        left = 0
        longest = 0

        for right, character in enumerate(s):
            while character in seen:
                seen.remove(s[left])
                left += 1

            seen.add(character)

            longest = max(longest, right - left + 1)

        return longest
