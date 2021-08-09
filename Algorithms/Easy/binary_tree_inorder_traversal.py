"""
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [1,2]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def builder(root: Optional[TreeNode], arr: List[int]) -> List[int]:
    if root != None:
        if root.left != None:
            builder(root.left, arr)
        if root.val != None:
            arr.append(root.val)
        if root.right != None:
            builder(root.right, arr)


class Traversal:
    def inorderTraversal(self, root: Optional[TreeNode], res: List[int]) -> List[int]:
        builder(root, res)
        return res


def makeTreeFromArray(arr: List[int], root: TreeNode, i: int) -> TreeNode:
    if i < len(arr):
        temp = TreeNode(arr[i])
        root = temp

        # insert left child
        root.left = makeTreeFromArray(arr, root.left, 2 * i + 1)

        # insert right child
        root.right = makeTreeFromArray(arr, root.right, 2 * i + 2)
    return root


if __name__ == "__main__":
    arr = [1, None, 2, 3]
    result = []
    root = None
    tree = makeTreeFromArray(arr, root, 0)
    print(Traversal().inorderTraversal(tree, result))
