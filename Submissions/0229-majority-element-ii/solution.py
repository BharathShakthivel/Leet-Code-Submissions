class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_dict = {}
        res =[]
        for i in nums:
            if i in freq_dict:
                freq_dict[i]+=1
            else:
                freq_dict[i]=1
        for j in freq_dict:
            if freq_dict[j]> (len(nums)//3):
                res.append(j)
        return res
