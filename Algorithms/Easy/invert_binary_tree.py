from typing import List

"""
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InvertTree:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return
        else:
            temp = root

            self.invertTree(root.left)
            self.invertTree(root.right)

            temp = root.left
            root.left = root.right
            root.right = temp

        return root


def makeTreeFromArray(
    root: TreeNode, arr: List[int], index: int, size: int
) -> TreeNode:
    if index < size:
        temp = TreeNode(arr[index])
        root = temp
        root.left = makeTreeFromArray(root.left, arr, 2 * index + 1, size)
        root.right = makeTreeFromArray(root.right, arr, 2 * index + 2, size)

    return root


def printLevelOrder(root: TreeNode) -> None:
    if root is None:
        return
    queue = []

    queue.append(root)

    while len(queue) > 0:

        print(queue[0].val, end=" ")
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    print("\n")


if __name__ == "__main__":
    arr = [4, 2, 7, 1, 3, 6, 9]
    n = len(arr)
    root = None
    tree = makeTreeFromArray(root, arr, 0, n)
    invert_tree = InvertTree().invertTree(tree)
    printLevelOrder(invert_tree)
