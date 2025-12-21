class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if len(strs) == 0:
        #     return ""
        # else:    
        #     base = strs[0]
        #     for i in range(len(base)):
        #         for word in strs[1:]:
        #             if (i == len(word) or word[i]!=base[i]):
        #                 return base[0:i]
        #     return base
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return res
            res+= strs[0][i]
        return res
