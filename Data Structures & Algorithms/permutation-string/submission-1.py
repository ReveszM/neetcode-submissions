class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        characterCount1 = defaultdict(int)
        curCharacterCount = defaultdict(int)
        for c in s1:
            characterCount1[c] += 1
        matches_required = len(list(characterCount1.keys()))
        
        cur_matches = 0
        l = 0
        for r in range(len(s2)):
            r_c = s2[r]
            l_c = s2[l]

            curCharacterCount[r_c] += 1
            if curCharacterCount[r_c] == characterCount1[r_c]:
                cur_matches += 1
            if curCharacterCount[r_c] - 1 == characterCount1[r_c]:
                cur_matches -= 1
            
            if r - l + 1 > len(s1):
                curCharacterCount[l_c] -= 1
                l += 1
                if curCharacterCount[l_c] == characterCount1[l_c]:
                    cur_matches += 1
                if curCharacterCount[l_c] + 1 == characterCount1[l_c]:
                    cur_matches -= 1

            if cur_matches == matches_required:
                return True
    
        return False
        