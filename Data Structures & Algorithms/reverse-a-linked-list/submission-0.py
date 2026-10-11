# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_forward = head
        place_holder = ListNode(-1)

        while cur_forward != None:
            new_node = ListNode(cur_forward.val)
            new_node.next = place_holder.next
            place_holder.next = new_node

            cur_forward = cur_forward.next
        return place_holder.next
        