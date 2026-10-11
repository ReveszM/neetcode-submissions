from math import trunc

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        r = []
        for t in tokens:
            if t == "+":
                a = r.pop()
                b = r.pop()
                r.append(a + b)
            elif t == "-":
                a = r.pop()
                b = r.pop()
                r.append(b - a)
            elif t == "*":
                a = r.pop()
                b = r.pop()
                r.append(a * b)
            elif t == "/":
                a = r.pop()
                b = r.pop()
                r.append(trunc(b/a))
            else:
                r.append(int(t))
        return r.pop()

        