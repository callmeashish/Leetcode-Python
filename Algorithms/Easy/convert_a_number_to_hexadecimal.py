"""
405. Convert a Number to Hexadecimal

Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.

 

Example 1:

Input: num = 26
Output: "1a"
Example 2:

Input: num = -1
Output: "ffffffff"
 

Constraints:

-231 <= num <= 231 - 1
"""


class ToHex:
    def toHex(self, num: int) -> str:
        if num < 0:
            num += 2 ** 32

        hexadecimal = "0123456789abcdef"
        hex_num = ""

        while num:
            num, rem = divmod(num, 16)
            hex_num = hexadecimal[rem] + hex_num

        return hex_num if hex_num else "0"


if __name__ == "__main__":
    print(ToHex().toHex(26))
