class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        window = set()

        L = 0
        for R in range(len(s)):
            if s[R] not in window:
                maxLen = max(maxLen, R - L + 1)
                window.add(s[R])
            else:
                while s[L] != s[R]:
                    window.remove(s[L])
                    L += 1
                L += 1


        return maxLen
        