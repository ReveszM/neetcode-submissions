# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchMin(self, root):
        while root != None and root.left != None:
            root = root.left
        return root
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                minNode = self.searchMin(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
                return root

        