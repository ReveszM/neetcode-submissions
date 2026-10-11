# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
            
        stack = [root]
        visit = [False]
        ret = []

        while len(stack) > 0:
            cur, cur_vis = stack.pop(), visit.pop()
            if cur_vis == False:
                stack.append(cur)
                visit.append(True)
                if cur.right != None:
                    stack.append(cur.right)
                    visit.append(False)
                if cur.left != None:
                    stack.append(cur.left)
                    visit.append(False)
            else: # cur_vis == True
                ret.append(cur.val)

        return ret

        
        