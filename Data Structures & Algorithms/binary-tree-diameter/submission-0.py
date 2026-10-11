# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathDiam(self, node):
        if node.right == None and node.left == None:
            return (0, 0)

        l = r = (-1, -1)
        if node.right != None:
            r = self.pathDiam(node.right)
        if node.left != None:
            l = self.pathDiam(node.left)
        maxPath = 1 + max(l[0], r[0])
        maxDiam = max(l[1], r[1], l[0] + r[0] + 2)
        return (maxPath, maxDiam)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root != None:
            return self.pathDiam(root)[1]
        else:
            return 0
        