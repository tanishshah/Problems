#563. Binary Tree Tilt
'''
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all
left subtree node values and all right subtree node values.
If a node does not have a left child, then the sum of the left subtree node
values is treated as 0. The rule is similar if there the node does not have
a right child.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    tilt = 0
    def summer(self,root:TreeNode) -> int:
        if root==None:
            return 0
        l = self.summer(root.left)
        r = self.summer(root.right)
        self.tilt += abs(l-r)
        return root.val + l + r
    def findTilt(self, root: TreeNode) -> int:
        self.summer(root)
        return self.tilt
