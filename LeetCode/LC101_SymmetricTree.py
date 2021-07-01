#101. Symmetric Tree
'''
Given the root of a binary tree, check whether it
is a mirror of itself (i.e., symmetric around its center).
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sym(self, l: TreeNode, r: TreeNode) -> bool:
        if l==None and r ==None:
            return True
        if l==None or r==None:
            return False
        if l.val != r.val:
            return 
        return self.sym(l.left,r.right) and self.sym(l.right,r.left)
    
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.sym(root.left,root.right)
