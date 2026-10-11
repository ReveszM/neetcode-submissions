# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curNode = head
        dummyNode = ListNode()
        
        while curNode != None and curNode != dummyNode:
            tmpNode = curNode
            curNode = curNode.next
            tmpNode.next = dummyNode

        return (curNode == dummyNode)
        