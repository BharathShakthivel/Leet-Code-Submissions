class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_dict = {}
        res = []
        n = len(nums)
        for i in nums:
            freq_dict[i] = 1 + freq_dict.get(i,0)
        for val,freq in freq_dict.items():
            if freq > (n/3):
                res.append(val)
        return res
        
