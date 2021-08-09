"""
344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.



Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.


Follow up: Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

from typing import List


class ReverseString:
    def reverseString1(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i = 0  # the first index of the array
        j = n-1  # the last index of the array

        while(i < j):
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s

    def reverseString2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        return s


if __name__ == "__main__":
    print(ReverseString().reverseString1(list("hello")))
    print(ReverseString().reverseString2(list("hello")))
