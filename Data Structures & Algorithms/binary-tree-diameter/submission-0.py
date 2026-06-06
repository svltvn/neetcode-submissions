# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
We need to keep track of the diameter and the height, which are not the same here
Height - longest path from each layer
Diameter - logest path from each node

We will set the maxDiameter in each recursive case, but then return through the maxHeight
Base Case:
if not node return 0

recursive case:
if node recurse down to right/left
return max(right, left)+1
'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def dfs(root):
            nonlocal maxDiameter
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            maxDiameter = max(maxDiameter, left+right)
            return max(left,right)+1
        
        dfs(root)
        return maxDiameter