class Solution:
    def encode(self, cur_str):
        code = [0] * 26
        for c in cur_str:
            code[ord(c) - ord('a')] += 1
        return code

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        codes = []

        for cur_str in strs:
            cur_code = self.encode(cur_str)

            added = False
            for i in range(len(ret)):
                if cur_code == codes[i]:
                    ret[i].append(cur_str)
                    added = True

            if not added:
                ret.append([cur_str])
                codes.append(cur_code)
        return ret

        