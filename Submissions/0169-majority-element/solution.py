class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # freq_dict = {}
        # for i in nums:
        #     if i in freq_dict:
        #         freq_dict[i]+=1
        #     else:
        #         freq_dict[i]=1
        # return max(freq_dict, key=freq_dict.get)
        nums.sort()
        return nums[len(nums)//2]

