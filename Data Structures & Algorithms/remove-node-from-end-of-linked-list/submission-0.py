# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = second = head
        prev = ListNode(next=head)
        for i in range(1, n):
            first = first.next
        while first.next:
            first = first.next
            prev = second
            second = second.next
        
        if prev.next != head:
            prev.next = prev.next.next
        else:
            head = head.next
        return head
        