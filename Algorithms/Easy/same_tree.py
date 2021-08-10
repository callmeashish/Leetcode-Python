"""
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class IsSameTree:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def makeTreeFromArray(arr: List[int], root: TreeNode, i: int) -> TreeNode:
    if i < len(arr):
        temp = TreeNode(arr[i])
        root = temp

        root.left = makeTreeFromArray(arr, root.left, 2 * i + 1)
        root.right = makeTreeFromArray(arr, root.right, 2 * i + 2)

    return root


if __name__ == "__main__":
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 3]

    tree1 = makeTreeFromArray(arr1, None, 0)
    tree2 = makeTreeFromArray(arr2, None, 0)

    print(IsSameTree().isSameTree(tree1, tree2))
