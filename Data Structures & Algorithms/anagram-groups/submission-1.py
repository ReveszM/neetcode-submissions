class Solution:
    def encode(self, cur_str):
        code = [0] * 26
        for c in cur_str:
            code[ord(c) - ord('a')] += 1
        return tuple(code)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        codes_strs = {}

        for cur_str in strs:
            cur_code = self.encode(cur_str)

            if cur_code in codes_strs:
                codes_strs[cur_code].append(cur_str)
            else:
                codes_strs[cur_code] = [cur_str]

        ret_val = []
        for cur_strs in codes_strs.values():
            ret_val.append(cur_strs)

        return ret_val

        