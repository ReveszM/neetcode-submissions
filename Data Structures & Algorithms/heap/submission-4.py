class MinHeap:
    
    def __init__(self):
        self.arr = [-1]
        

    def push(self, val: int) -> None:
        if len(self.arr) == 0:
            self.arr = [0]

        self.arr.append(val)
        cur = len(self.arr) - 1
        while cur > 1:
            parent = cur // 2
            if self.arr[parent] > self.arr[cur]:
                self.arr[cur], self.arr[parent] = self.arr[parent], self.arr[cur]
                cur = parent
            else:
                break

    def pop(self) -> int:
        if len(self.arr) <= 1:
            return -1
        elif len(self.arr) == 2:
            return self.arr.pop()

        ret = self.arr[1]
        self.arr[1] = self.arr.pop()
        cur = 1
        while 2 * cur <= len(self.arr) - 1:
            lc = 2 * cur
            rc = 2 * cur + 1
            if (rc <= len(self.arr) - 1 and
            self.arr[cur] > self.arr[rc] and
            self.arr[rc] <= self.arr[lc]):
                self.arr[cur], self.arr[rc] = self.arr[rc], self.arr[cur]
                cur = rc
            elif self.arr[cur] > self.arr[lc]:
                self.arr[cur], self.arr[lc] = self.arr[lc], self.arr[cur]
                cur = lc
            else:
                break
        return ret
        

    def top(self) -> int:
        if len(self.arr) > 1:
            return self.arr[1]
        else:
            return -1
        

    def heapify(self, nums: List[int]) -> None:
        self.arr = [0]
        self.arr.extend(nums)

        for i in range(len(self.arr) - 1, 0, -1):
            cur = i
            while 2 * cur <= len(self.arr) - 1:
                lc = 2 * cur
                rc = 2 * cur + 1
                if (rc <= len(self.arr) - 1 and
                self.arr[cur] > self.arr[rc] and
                self.arr[rc] <= self.arr[lc]):
                    self.arr[cur], self.arr[rc] = self.arr[rc], self.arr[cur]
                    cur = rc
                elif self.arr[cur] > self.arr[lc]:
                    self.arr[cur], self.arr[lc] = self.arr[lc], self.arr[cur]
                    cur = lc
                else:
                    break 
        
        