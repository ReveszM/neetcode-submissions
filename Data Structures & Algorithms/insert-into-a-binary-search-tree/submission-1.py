# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val = val)
        
        cur = root

        while True:
            if cur.val > val:
                if cur.left == None:
                    cur.left = TreeNode(val)
                    break
                else:
                    cur = cur.left
            elif cur.val < val:
                if cur.right == None:
                    cur.right = TreeNode(val)
                    break
                else:
                    cur = cur.right
        
        return root
        