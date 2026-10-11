class Solution:
    def isValid(self, s: str) -> bool:
        pstack = []
        for c in s:
            if c in {"(", "[", "{"}:
                pstack.append(c)
            elif c == ")":
                if len(pstack) < 1 or pstack.pop() != "(":
                    return False
            elif c == "]":
                if len(pstack) < 1 or pstack.pop() != "[":
                    return False
            elif c == "}":
                if len(pstack) < 1 or pstack.pop() != "{":
                    return False

        return (len(pstack) == 0)
        