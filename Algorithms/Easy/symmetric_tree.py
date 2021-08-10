"""
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def match(left: TreeNode, right: TreeNode):
    if left == None or right == None:
        return left == right
    if left.val != right.val:
        return False
    else:
        return match(left.left, right.right) and match(left.right, right.left)


class IsSymmetric:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return match(root.left, root.right)


def makeTreeFromArray(arr, root, i):
    if i < len(arr):
        temp = TreeNode(arr[i])
        root = temp

        root.left = makeTreeFromArray(arr, root.left, 2 * i + 1)
        root.right = makeTreeFromArray(arr, root.right, 2 * i + 2)

    return root


if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 3]
    tree = makeTreeFromArray(arr, None, 0)
    print(IsSymmetric().isSymmetric(tree))
