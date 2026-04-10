class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_dict = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prev_dict:
                return [prev_dict[diff],i]
            prev_dict[n] = i
        return

        # my_dict ={}
        # for i,v in enumerate(nums):
        #     diff = target - v
        #     if diff in my_dict:
        #         return [my_dict[diff],i]
        #     my_dict[v] = i    
        # return
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i,j


