"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false
 

Constraints:

-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
"""


class Solution:
    def isPalindromeStringSolution(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    def isPalindromeNumberSolution(self, x: int) -> bool:
        number = x
        reverse = 0
        if x < 0:
            return False
        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = int(x / 10)
        if number == reverse:
            return True
        else:
            return False


if __name__ == "__main__":
    print(Solution().isPalindromeNumberSolution(121))
