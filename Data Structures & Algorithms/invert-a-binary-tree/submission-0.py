# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(root):
    if root == None:
        return
    tmp = root.right
    root.right = root.left
    root.left = tmp

    dfs(root.left)
    dfs(root.right)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dfs(root)
        return root
        