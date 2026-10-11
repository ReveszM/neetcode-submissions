class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += 1

        counts = list(num_count.values())
        counts.sort(reverse = True)

        limit = counts[k - 1]

        result = []
        for (num, count) in num_count.items():
            if count >= limit:
                result.append(num)

        return result

        

        
        