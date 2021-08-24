"""
504. Base 7

Given an integer num, return a string of its base 7 representation.

Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"
 

Constraints:

-107 <= num <= 107

"""


class Base:
    def convertToBase7(self, num: int) -> str:
        base = ""
        x = 0
        n = abs(num)
        while n > 6:
            n, x = divmod(n, 7)
            base = str(x) + base

        base = str(n) + base

        return "-" + base if num < 0 else base
