# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        cur_merge = None
        ret_val = None
        
        if list1.val <= list2.val:
            cur_merge = list1
            ret_val = list1
            list1 = list1.next
        else:
            cur_merge = list2
            ret_val = list2
            list2 = list2.next

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                cur_merge.next = list1
                cur_merge = list1
                list1 = list1.next
            else:
                cur_merge.next = list2
                cur_merge = list2
                list2 = list2.next
        if list1 == None:
            cur_merge.next = list2
        else:
            cur_merge.next = list1
        
        return ret_val          


        