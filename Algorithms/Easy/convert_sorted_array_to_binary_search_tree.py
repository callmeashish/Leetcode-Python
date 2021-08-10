"""
108. Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
"""


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printTree(root, res):
    if root != None:
        printTree(root.left, res)
        if root.val != None:
            res.append(root.val)
        printTree(root.right, res)
    return res


def makeTree(arr, left, right) -> TreeNode:
    if left > right:
        return None

    mid = left + (right - left) // 2
    root = TreeNode(arr[mid])

    root.left = makeTree(arr, left, mid - 1)
    root.right = makeTree(arr, mid + 1, right)

    return root


class SortedArrayToBST:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        tree = makeTree(nums, 0, len(nums) - 1)
        return tree


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    res = []
    tree = SortedArrayToBST().sortedArrayToBST(nums)
    print(printTree(tree, res))
