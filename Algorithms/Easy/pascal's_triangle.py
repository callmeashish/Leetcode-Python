"""
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
"""

from typing import List


class Pascal:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        row = [[1], [1, 1]]
        for i in range(2, numRows):
            column = [row[i - 1][j - 1] + row[i - 1][j] for j in range(1, i)]
            column.insert(0, 1)
            column.append(1)
            row.append(column)
        return row


if __name__ == "__main__":
    numRows = 5
    print(Pascal().generate(numRows))
