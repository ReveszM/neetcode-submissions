class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        answerIdxs = (-1, -1)
        for i in range(len(s)):
            # odd
            l = r = i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if maxLen < r - l + 1:
                    maxLen = r - l + 1
                    answerIdxs = (l , r)
                l -= 1
                r += 1

            # even
            l = i
            r = i + 1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if maxLen < r - l + 1:
                    maxLen = r - l + 1
                    answerIdxs = (l , r)
                l -= 1
                r += 1

        return s[answerIdxs[0] : answerIdxs[1] + 1]
        