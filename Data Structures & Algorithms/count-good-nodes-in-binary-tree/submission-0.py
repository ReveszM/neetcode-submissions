# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def count(self, root, maxVal):
        if root == None:
            return 0
        else:
            curCount = 1 if root.val >= maxVal else 0
            leftCount = self.count(root.left, max(maxVal, root.val))
            rightCount = self.count(root.right, max(maxVal, root.val))
            return curCount + leftCount + rightCount
        

    def goodNodes(self, root: TreeNode) -> int:
        return self.count(root, -101)
