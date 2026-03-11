"""20. Valid Parentheses.

https://leetcode.com/problems/valid-parentheses/description/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {"(": ")", "{": "}", "[": "]"}

        for character in s:
            if character in pairs:
                stack.append(character)

            if character in pairs.values():
                if not stack:
                    return False

                opening_bracket = stack.pop()

                if (
                    (opening_bracket == "(" and character == pairs["("])
                    or (opening_bracket == "{" and character == pairs["{"])
                    or (opening_bracket == "[" and character == pairs["["])
                ):
                    continue

                return False

        return not stack
