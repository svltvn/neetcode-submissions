# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = {}
        layer = 0

        def bfs(root, layer):
            if not root:
                return
            
            hashmap.setdefault(layer, []).append(root.val)
            layer +=1
            bfs(root.left, layer)
            bfs(root.right, layer)
        
        
        bfs(root, layer)
        print(hashmap)
        res = []
        for layer, vals in hashmap.items():
            res.insert(layer, vals)
        
        return res