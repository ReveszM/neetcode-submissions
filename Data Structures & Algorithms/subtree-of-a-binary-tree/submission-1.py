# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkTree(root, subRoot):
            if root == None:
                return (subRoot == None)
            elif subRoot == None:
                return False

            if root.val == subRoot.val:
                return (checkTree(root.left, subRoot.left) 
                and checkTree(root.right, subRoot.right))
            else:
                return False

        def dfs(node):
            if node == None:
                return False
            return (checkTree(node, subRoot)
            or dfs(node.left) 
            or dfs(node.right))
        
        return dfs(root)


            
        