"""
415. Add Strings

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
 

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""


class AddStrings:
    @staticmethod
    def addStrings(num1: str, num2: str) -> str:
        carry = 0
        length = 0
        res = ""

        m = len(num1)
        n = len(num2)

        exe = abs(m - n)

        if m >= n:
            num2 = "0" * exe + num2
            length = m
        elif m < n:
            num1 = "0" * exe + num1
            length = n

        for index in range(length - 1, -1, -1):
            add_sum = int(num1[index]) + int(num2[index]) + carry
            carry, digit = divmod(add_sum, 10)
            res = str(digit) + res

        if carry != 0:
            res = str(carry) + res

        return res


if __name__ == "__main__":
    num1 = "1"
    num2 = "9"
    print(AddStrings.addStrings(num1, num2))
