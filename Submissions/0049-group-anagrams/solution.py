class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # freq_dict = defaultdict(list)   
        # for s in strs:
        #     str_count = [0] * 26
        #     for c in s:
        #         str_count[ord(c) - ord('a')] += 1
        #     key = tuple(str_count)
        #     freq_dict[key].append(s)
        

        # return list(freq_dict.values())
        
        # # Dealing with sorting method
        # ans = defaultdict(list)
        # for s in strs:
        #     key = "".join(sorted(s))
        #     ans[key].append(s)
        # return list(ans.values())


















        # Practise
        my_dict = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for i in s:
                key[ord("a")-ord(i)]+=1
            my_dict[tuple(key)].append(s)
        return list(my_dict.values())

