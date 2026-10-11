# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        solution_head = ListNode(0)
        solution_current = solution_head
        carry = 0
        first = True

        while l1 != None or l2 != None or carry != 0:
            if l1 != None:
                a = l1.val
                l1 = l1.next
            else:
                a = 0

            if l2 != None:
                b = l2.val
                l2 = l2.next
            else:
                b = 0

            cur_digit = (a + b + carry) % 10
            carry = int(((a + b + carry) - cur_digit) / 10)

            if first:
                solution_current.val = cur_digit
                first = False
            else:
                solution_current.next = ListNode(cur_digit)
                solution_current = solution_current.next         

        return solution_head