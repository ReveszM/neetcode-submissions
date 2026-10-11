# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        todo = [(root, False)]
        height = {None: 0}

        while len(todo) > 0:
            curNode, visited = todo.pop()
            
            if visited:
                if abs(height[curNode.left] - height[curNode.right]) > 1:
                    return False
                height[curNode] = 1 + max(height[curNode.left], height[curNode.right])
            else:
                todo.append((curNode, True))
                if curNode.left != None:
                    todo.append((curNode.left, False))
                if curNode.right != None:
                    todo.append((curNode.right, False))
        return True


        