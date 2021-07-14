"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        if x > 0:
            reverse = int(str(x)[::-1])
        else:
            reverse = -int(str(abs(x))[::-1])

        if reverse < -2147483648 or reverse > 2147483647:
            return 0
        else:
            return int(reverse)


if __name__ == "__main__":
    print(Solution().reverse(123))
