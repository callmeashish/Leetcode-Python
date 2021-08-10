"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def calculateDepth(root: TreeNode):
    if not root:
        return 0
    leftHeight = calculateDepth(root.left)
    rightHeight = calculateDepth(root.right)

    if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
        return -1
    return 1 + max(leftHeight, rightHeight)


class IsBalanced:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return calculateDepth(root) != -1


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(IsBalanced().isBalanced(root))
