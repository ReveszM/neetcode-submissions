# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rec(self, root):
        if root:
            (leftMaxOne, leftTwo, leftExcl) = self.rec(root.left)
            (rightMaxOne, rightTwo, rightExcl) = self.rec(root.right)
            rootMaxOne = root.val + max(0, leftMaxOne, rightMaxOne)
            rootTwo = root.val + leftMaxOne + rightMaxOne
            rootExcl = max(leftMaxOne, leftTwo, leftExcl, rightMaxOne, rightTwo, rightExcl)
            return (rootMaxOne, rootTwo, rootExcl)
        else:
            return (-1001, -1001, -1001)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return max(self.rec(root))

        