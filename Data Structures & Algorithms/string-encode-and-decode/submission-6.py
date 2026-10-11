class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        starts = [0] * len(strs)
        starts[-1] = (-1) * len(strs[-1])
        for i in range(2, len(strs) + 1):
            curStr = strs[-i]
            starts[-i] = starts[-(i - 1)] + (-1) * len(curStr)

        r = ""
        for curStart in starts:
            r += str(curStart)
        r += "-*"
        for curStr in strs:
            r += curStr
        return r

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        startIdxs = []
        curIdxStr = ""
        prevIdx = 0
        start = 1 if s[0] == "-" else 0
        for i in range(start, len(s)):
            if s[i] == "*":
                break
            elif s[i] != "-":
                curIdxStr += s[i]
            elif s[i] == "-":
                curIdx = int(curIdxStr) * (-1)
                startIdxs.append(curIdx)
                prevIdx = curIdx
                curIdxStr = ""
        
        r = []
        for i in range(0, len(startIdxs)):
            startIdx = startIdxs[i]
            endIdx = startIdxs[i + 1] if i < len(startIdxs) - 1 else 0
            curStr = ""
            for j in range(startIdx, endIdx):
                curStr += s[j]
            r.append(curStr)
        return r




