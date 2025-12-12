class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_dict = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prev_dict:
                return [prev_dict[diff],i]
            prev_dict[n] = i
        return
