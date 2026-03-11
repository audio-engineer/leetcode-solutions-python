"""155. Min Stack.

https://leetcode.com/problems/min-stack/description/
"""

from leetcode.min_stack import MinStack


def test_length_of_longest_substring() -> None:
    stack = MinStack()

    stack.push(-2)
    stack.push(0)
    stack.push(-3)

    assert stack.getMin() == -3

    stack.pop()

    assert stack.top() == 0
    assert stack.getMin() == -2

    stack.pop()
    stack.pop()

    stack.push(0)
    stack.push(1)
    stack.push(0)

    assert stack.getMin() == 0

    stack.pop()

    assert stack.getMin() == 0

    stack.pop()

    assert stack.getMin() == 0

    stack.pop()

    stack.push(-2)
    stack.push(-1)
    stack.push(-2)

    assert stack.getMin() == -2

    stack.pop()

    assert stack.top() == -1
    assert stack.getMin() == -2

    stack.pop()

    assert stack.getMin() == -2

    stack.pop()
