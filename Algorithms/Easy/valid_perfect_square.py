"""
367. Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
 

Constraints:

1 <= num <= 2^31 - 1
"""

import math


class IsPerfectSquare:

    # Binary Implementation
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        while low <= high:
            mid = (low+high) >> 1
            if mid*mid > num:
                high = mid-1
            elif mid*mid < num:
                low = mid+1
            else:
                return True
        return False


if __name__ == '__main__':
    print(IsPerfectSquare().isPerfectSquare(808201))
