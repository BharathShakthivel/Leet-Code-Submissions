class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dict = defaultdict(list)   
        for s in strs:
            str_count = [0] * 26
            for c in s:
                str_count[ord(c) - ord('a')] += 1
            key = tuple(str_count)
            freq_dict[key].append(s)
        

        return list(freq_dict.values())
