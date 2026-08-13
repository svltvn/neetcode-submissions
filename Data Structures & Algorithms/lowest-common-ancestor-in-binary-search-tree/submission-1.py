# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #whenever we have to split root node, we know we are at the LCA
        if root.val < p.val and root.val < q.val:
            node = self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            node = self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


        return node    