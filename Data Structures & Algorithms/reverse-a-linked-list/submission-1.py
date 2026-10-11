# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_forward = head
        head_reverse = None

        while cur_forward != None:
            next_forward = cur_forward.next
            cur_forward.next = head_reverse
            head_reverse = cur_forward

            cur_forward = next_forward
        return head_reverse
        