# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
So, this problem is like the one before, but instead, we would only see if the subtree
and it's node match with the tree once we have found the same value of subRoot tree
'''
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if (not root and subRoot) or (not subRoot and root):
            return False
        
        if root.val == subRoot.val:
            sameTree = self.sameTree(root, subRoot)
            if sameTree:
                return True
            else:
                right = self.isSubtree(root.right, subRoot)
                left = self.isSubtree(root.left, subRoot)
                return right or left
        else:
            right = self.isSubtree(root.right, subRoot)
            left = self.isSubtree(root.left, subRoot)
            return right or left
    
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if (not root and subRoot) or (root and not subRoot):
            return False
        
        if root.val == subRoot.val:
            left = self.sameTree(root.left, subRoot.left)
            right = self.sameTree(root.right, subRoot.right)

            return left and right
        else:
            return False

    
    
