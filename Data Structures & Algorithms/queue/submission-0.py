class LLNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return (self.head == None)
        

    def append(self, value: int) -> None:
        if self.tail != None:
            self.tail.next = LLNode(value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        else:
            self.tail = LLNode(value)
            self.head = self.tail
        

    def appendleft(self, value: int) -> None:
        if self.head != None:
            self.head.prev = LLNode(value)
            self.head.prev.next = self.head
            self.head = self.head.prev
        else:
            self.head = LLNode(value)
            self.tail = self.head
        

    def pop(self) -> int:
        if self.tail != None:
            r = self.tail.val
            self.tail = self.tail.prev
            if self.tail != None:
                self.tail.next = None
            else:
                self.head = None
            return r
        else:
            return -1
        
    def popleft(self) -> int:
        if self.head != None:
            r = self.head.val
            self.head = self.head.next
            if self.head != None:
                self.head.prev = None
            else:
                self.tail = None
            return r
        else:
            return -1
        
