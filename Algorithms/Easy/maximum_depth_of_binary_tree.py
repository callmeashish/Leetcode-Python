"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
Example 3:

Input: root = []
Output: 0
Example 4:

Input: root = [0]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaxDepth:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return max(leftDepth, rightDepth) + 1


def printTree(root):

    if root:
        print(root.val, end=" ")

        printTree(root.left)

        printTree(root.right)


def makeTreeFromArray(arr, root, i):
    if i < len(arr) and arr[i] != None:
        temp = TreeNode(arr[i])
        root = temp

        root.left = makeTreeFromArray(arr, root.left, 2 * i + 1)
        root.right = makeTreeFromArray(arr, root.right, 2 * i + 2)

    return root


if __name__ == "__main__":
    arr = [1, None, 2]
    tree = makeTreeFromArray(arr, None, 0)
    print(MaxDepth().maxDepth(tree))
