class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        s = ['a'] * (2 * n)
    
        def r(i, openingP, closingP):
            if i == (2 * n):
                ret.append(''.join(s))
                return
            
            if openingP > closingP and closingP < n:
                s[i] = ')'
                r(i + 1, openingP, closingP + 1)
            if openingP < n:
                s[i] = '('
                r(i + 1, openingP + 1, closingP)

        r(0, 0, 0)


        return ret
        