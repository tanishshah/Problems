#111. Minimum Depth of Binary Tree
'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        depth = 0
        if root==None:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        depth = min(l,r) + 1
        if l and r:
            return depth
        return l+r+1
