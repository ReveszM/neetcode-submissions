#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.nodes = []

    def calculateIdx(self, i):
        if i % 2 == 0:
            curIdx = i / 2
        else: # i % 2 == 1
            tmp = (i - 1) / 2
            curIdx = len(self.nodes) - 1 - tmp
        return int(curIdx)

    
    def reorderList(self, head: Optional[ListNode]) -> None:
        curNode = head
        while curNode != None:
            self.nodes.append(curNode)
            curNode = curNode.next

        for i in range(len(self.nodes) - 1):
            curIdx = self.calculateIdx(i)
            nextIdx = self.calculateIdx(i + 1)
            self.nodes[curIdx].next = self.nodes[nextIdx]

        lastIdx = self.calculateIdx(len(self.nodes) - 1)
        self.nodes[lastIdx].next = None

        return None
            


        

        

        