class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,h = 0 , len(nums)-1
        while l <=h:
            mid = l + ((h-l)//2)
            mid_num = nums[mid]
            if mid_num == target:
                return mid
            if mid_num < target:
                l = mid + 1
            elif mid_num > target:
                h = mid - 1
        return -1
