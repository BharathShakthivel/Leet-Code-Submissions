class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # for index,value in enumerate(nums):
        #     if value == target:
        #         return index
        #     elif value > target:
        #         return index
        # return len(nums)
        
        l,h = 0 , len(nums)-1
        while l <=h:
            mid = l + ((h-l) // 2)
            mid_num = nums[mid]
            if mid_num == target:
                return mid
            elif mid_num > target:
                h = mid - 1
            elif mid_num < target:
                l = mid + 1
        return l
