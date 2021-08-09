"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        end_dict = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in end_dict.values():
                stack.append(char)
            else:
                if stack == []:
                    return False
                prev = stack.pop()
                if not end_dict[char] == prev:
                    return False
        if stack == []:
            return True
        return False


if __name__ == "__main__":
    print(Solution().isValid("{[]}"))
