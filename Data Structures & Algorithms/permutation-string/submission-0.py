class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        characterCount1 = {}
        curCharacterCount = {}

        for c in s1:
            if c in characterCount1:
                characterCount1[c] += 1
            else:
                characterCount1[c] = 1
            curCharacterCount[c] = 0
        for c in s2:
            if c not in s1:
                characterCount1[c] = 0
            curCharacterCount[c] = 0

        l = 0
        for r in range(len(s2)):
            curCharacterCount[s2[r]] += 1
            if r - l + 1 > len(s1):
                curCharacterCount[s2[l]] -= 1
                l += 1
            if curCharacterCount == characterCount1:
                return True
    
        return False
        