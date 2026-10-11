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
        dummy = TreeNode(val = -1, right = root)
        right = True
        cur = root
        prev = dummy

        while cur != None:
            if cur.val < key:
                prev = cur
                cur = cur.right
                right = True
            elif cur.val > key:
                prev = cur
                cur = cur.left
                right = False
            else:
                if cur.right == None:
                    if right:
                        prev.right = cur.left
                    else:
                        prev.left = cur.left
                    break
                elif cur.left == None:
                    if right:
                        prev.right = cur.right
                    else:
                        prev.left = cur.right
                    break
                else:
                    minNode = self.searchMin(cur.right)
                    cur.val = minNode.val
                    key = minNode.val
                    prev = cur
                    cur = cur.right
                    right = True
                
        return dummy.right

        