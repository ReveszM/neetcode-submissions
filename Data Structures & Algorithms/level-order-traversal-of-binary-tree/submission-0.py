# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []

        todo = deque()
        if root != None:
            todo.append(root)

        while len(todo) > 0:
            level = []

            for i in range(len(todo)):
                node = todo.popleft()
                level.append(node.val)
                if node.left != None:
                    todo.append(node.left)
                if node.right != None:
                    todo.append(node.right)
            ret.append(level)

        return ret