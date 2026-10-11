class LLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def getNode(self, index):
        cur = self.head
        i = 0
        while cur != None and i < index:
            cur = cur.next
            i += 1
        return cur
    
    def get(self, index: int) -> int:
        node = self.getNode(index)
        if node != None:
            return node.value
        else:
            return -1
        
    def insertHead(self, val: int) -> None:
        node = LLNode(val)
        if self.head != None:
            node.next = self.head
        else:
            self.tail = node
        self.head = node

    def insertTail(self, val: int) -> None:
        node = LLNode(val)
        if self.tail != None:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def remove(self, index: int) -> bool:
        if index == 0:
            if self.head == None:
                return False
            elif self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        else:
            prev_node = self.getNode(index - 1)
            if prev_node == None or prev_node == self.tail:
                return False
            if prev_node.next == self.tail:
                self.tail = prev_node
                prev_node.next = None
            else:
                prev_node.next = prev_node.next.next
        return True

    def getValues(self) -> List[int]:
        ret = []
        cur = self.head
        while cur != None:
            ret.append(cur.value)
            cur = cur.next
        return ret
        
