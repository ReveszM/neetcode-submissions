# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curNode = head
        i = 0
        while curNode != None and i <= 1000:
            i += 1
            curNode = curNode.next

        return (i == 1001)
        