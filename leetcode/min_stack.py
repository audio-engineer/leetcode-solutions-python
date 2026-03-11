"""155. Min Stack.

https://leetcode.com/problems/min-stack/description/
"""


class MinStack:
    stack: list[int]
    where_min: list[int]

    def __init__(self) -> None:
        self.stack = []
        self.where_min = [0]

    def push(self, val: int) -> None:
        self.stack.append(val)

        if val < self.stack[self.where_min[-1]]:
            self.where_min.append(len(self.stack) - 1)

            return

        if val >= self.stack[self.where_min[-1]]:
            self.where_min.append(self.where_min[-1])

    def pop(self) -> None:
        if not self.stack and not self.where_min:
            return

        self.stack.pop()
        self.where_min.pop()

    def top(self) -> int:
        if not self.stack and not self.where_min:
            return 0

        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack and not self.where_min:
            return 0

        return self.stack[self.where_min[-1]]
