class Solution:
    def __init__(self):
        self.window = defaultdict(int)
        self.maxCharacter = -1
    
    def updateMaxCharacter(self):
        for (curChar, curCount) in self.window.items():
            if curCount > self.window[self.maxCharacter]:
                self.maxCharacter = curChar

    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        L = 0

        for R in range(len(s)):
            self.window[s[R]] += 1
            if self.window[s[R]] > self.window[self.maxCharacter]:
                self.maxCharacter = s[R]
            while not R - L + 1 - self.window[self.maxCharacter] <= k:
                self.window[s[L]] -= 1
                self.updateMaxCharacter()
                L += 1
            maxLen = max(maxLen, R - L + 1)
        
        return maxLen
            


        