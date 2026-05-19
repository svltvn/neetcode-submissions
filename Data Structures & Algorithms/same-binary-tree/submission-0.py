# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        valid = True
        if p == None and q == None:
            return True
        elif (p and q == None) or (p == None and q):
            return False
        if (q.val == p.val):
            right = self.isSameTree(p.right, q.right)
            left = self.isSameTree(p.left, q.left)
            valid = right and left
        else:
            valid = False
        
        return valid