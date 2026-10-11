# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(a, b):
            if a == None and b == None:
                return True
            elif a == None and b != None:
                return False
            elif a != None and b == None:
                return False

            if a.val != b.val:
                return False

            return dfs(a.left, b.left) and dfs(a.right, b.right)
        
        return dfs(p, q)
        