#94. Binary Tree Inorder Traversal
'''
Given the root of a binary tree, return the inorder traversal
of its nodes' values.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def traverse(self,root: TreeNode,l):
        if root==None:
            return
        self.traverse(root.left,l)
        l.append(root.val)
        self.traverse(root.right,l)
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
        self.traverse(root,l)
        return(l)
