# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, node):
        if node == None:
            return 0
        else:
            return max(self.depth(node.left), self.depth(node.right)) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root)
        