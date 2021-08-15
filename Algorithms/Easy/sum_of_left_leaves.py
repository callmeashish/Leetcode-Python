"""
404. Sum of Left Leaves

Given the root of a binary tree, return the sum of all left leaves.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False


class Leftleaves:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0

        if root is not None:

            if isLeaf(root.left):
                res += root.left.val
            else:
                res += self.sumOfLeftLeaves(root.left)

            res += self.sumOfLeftLeaves(root.right)
        return res


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(Leftleaves().sumOfLeftLeaves(root))
