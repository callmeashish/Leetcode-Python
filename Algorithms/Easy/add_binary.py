"""
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


class AddBinary:
    def addBinary(self, a: str, b: str) -> str:
        n = len(a)
        m = len(b)

        diff = abs(n-m)

        if n > m:
            b = "0"*diff + b
        else:
            a = "0"*diff + a

        result = ""

        carry = 0

        for i in range(len(a)-1, -1, -1):
            bit_sum = int(a[i]) + int(b[i]) + carry
            result = str(bit_sum % 2) + result
            carry = bit_sum // 2

        if carry != 0:
            result = str(carry)+result

        return result


if __name__ == '__main__':
    print(AddBinary().addBinary("1010", "1011"))
