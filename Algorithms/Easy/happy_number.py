"""
202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1
"""


class Solution:
    def calcSquareSum(self, number: int, search: set) -> int:
        square_sum = 0
        for num in str(number):
            square_sum += int(num) ** 2

        if square_sum != 1 and square_sum not in search:
            search.add(square_sum)
            return self.calcSquareSum(square_sum, search)

        return int(square_sum) == 1

    def isHappy(self, n: int) -> bool:
        search = set()
        return self.calcSquareSum(n, search)


if __name__ == "__main__":
    print(Solution().isHappy(2))
