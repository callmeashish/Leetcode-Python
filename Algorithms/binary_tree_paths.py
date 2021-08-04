"""
257. Binary Tree Paths

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreePaths:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = dfs(root, "", [])

        return res


def dfs(root, string, arr):
    string += str(root.val)
    if not root.left and not root.right:
        arr.append(string)

    if root.left:
        dfs(root.left, string + "->", arr)
    if root.right:
        dfs(root.right, string + "->", arr)

    return arr


def makeTreeFromArray(root: TreeNode, arr: List[int], index: int) -> TreeNode:
    if index < len(arr) and arr[index] != None:
        node = TreeNode(arr[index])
        root = node

        root.left = makeTreeFromArray(root.left, arr, 2 * index + 1)
        root.right = makeTreeFromArray(root.right, arr, 2 * index + 2)

    return root


def lvlPrint(root: TreeNode) -> None:
    if root is None:
        return
    queue = []
    queue.append(root)

    while len(queue) > 0:

        print(queue[0].val)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)


if __name__ == "__main__":
    arr = [1, 2, 3, None, 5]
    root = None

    tree = makeTreeFromArray(root, arr, 0)
    print(BinaryTreePaths().binaryTreePaths(tree))
