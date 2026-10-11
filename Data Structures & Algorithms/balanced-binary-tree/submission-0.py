# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def heightBalanced(node):
            a = b = (0, True)
            if node.left != None:
                a = heightBalanced(node.left)
            if node.right != None:
                b = heightBalanced(node.right)

            ret = (1 + max(a[0], b[0]), 
            a[1] and b[1] and abs(a[0] - b[0]) <= 1)
            return ret

        if root != None:
            return heightBalanced(root)[1]
        else:
            return True
        