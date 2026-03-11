"""567. Permutation in String.

https://leetcode.com/problems/permutation-in-string/description/
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = [0] * 26
        freq_substring = [0] * 26

        for character in s1:
            freq_s1[ord(character) - ord("a")] += 1

        for index, character in enumerate(s2):
            character_value = ord(character) - ord("a")

            if freq_s1[character_value] > 0:
                for substring_index in range(index, index + len(s1)):
                    if substring_index < len(s2):
                        freq_substring[ord(s2[substring_index]) - ord("a")] += 1

                if freq_substring != freq_s1:
                    freq_substring = [0] * 26
                else:
                    return True

        return False
