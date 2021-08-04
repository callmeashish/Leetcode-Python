"""
258. Add Digits

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1
"""


class AddDigits:
    def addDigits(self, num: int) -> int:
        num_sum = 0
        if (num <= 9):
            return num
        while(num != 0):
            num_sum += num % 10
            num = num // 10
        return self.addDigits(num_sum)


if __name__ == '__main__':
    num = 38
    print(AddDigits().addDigits(num))
