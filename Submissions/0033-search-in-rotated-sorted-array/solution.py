class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute Force: O(N)
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1
        

        # My Optimal Approach to undertand

        # We will find a pivot
        l,r = 0 ,len(nums)-1
        while l<r:
            m = (l+r)//2
            # [4,5,6,7,0,1,2] Example
            if nums[m] > nums[r]:
                l =m+1
            else:
                r =m
        # When the loop ends either L or R will point to the same min value index (Pivot)of the array
        pivot = l

        #Edge Case when the array is not rotated at all, so the pivot might be 0 which is the starting of the array,
        # In that case we perform the normal binary search.
        if pivot == 0:
            l,r = pivot,len(nums)-1
        elif target<=nums[pivot-1] and target>=nums[0]:
            l,r = 0,pivot-1
        else:
            l,r=pivot,len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        return -1


        # Binary Search (One pass) (HARD TO UNDERSTAND) Time (logn) Space = O(1)
        
        # l = 0
        # r = len(nums)-1

        # while l<=r:
        #     mid = (l+r)//2
        #     if target == nums[mid]:
        #         return mid
        #     if nums[l]<= nums[mid]:
        #         if target<nums[l] or target>nums[mid]:
        #             l=mid+1
        #         else:
        #             r=mid-1
        #     else:
        #         if target<nums[mid] or target > nums[r]:
        #             r=mid-1
        #         else:
        #             l=mid+1
        # return -1


