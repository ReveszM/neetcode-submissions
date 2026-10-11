class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.count = [0 for _ in range(2001)] # idx = 1000 + i
        self.count_sum = 0

        for num in nums:
            self.count[1000 + num] += 1

        self.kth = 1000
        self.count_sum += self.count[1000 + self.kth]
        while self.kth > -1000 and self.count_sum < self.k:
            self.kth -= 1
            self.count_sum += self.count[1000 + self.kth]
        
    def add(self, val: int) -> int:
        if val < self.kth:
            return self.kth
        else: #val >= self.kth:
            self.count[1000 + val] += 1
            self.count_sum += 1

            if self.count_sum - self.count[1000 + self.kth] >= self.k:
                self.count_sum -= self.count[1000 + self.kth]
                self.kth += 1
                while self.count[1000 + self.kth] == 0:
                    self.kth += 1
            return self.kth
        
        
