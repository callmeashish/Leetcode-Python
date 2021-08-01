"""
171. Excel Sheet Column Number

Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
Example 4:

Input: columnTitle = "FXSHRXW"
Output: 2147483647
 

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
"""


class Solution:
    @staticmethod
    def titleToNumber1(columnTitle: str) -> int:
        total = 0
        for char in columnTitle:
            total = total * 26 + (ord(char) % 64)
        return total

    def titleToNumber2(columnTitle: str) -> int:
        ans = 0
        for i in columnTitle:
            ans = ans * 26 + ord(i) - ord("A") + 1
        return ans


if __name__ == "__main__":
    columnNumber = "AB"
    print(Solution.titleToNumber1(columnNumber))
    print(Solution.titleToNumber2(columnNumber))
