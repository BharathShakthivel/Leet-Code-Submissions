class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # nums = set(nums)
        # if target in nums:
        #     return True
        # return False

        l,r = 0, len(nums)-1

        while l<=r:
            mid = l + ((r-l)//2)
            if nums[mid] == target:
                return True
            # LEFT PORTION IS SORTED
            if nums[l]<nums[mid]:
                # Checking if Target belongs to the left Portion:
                if nums[l]<=target<nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            # RIGHT PORTION IS SORTED
            elif nums[l]>nums[mid]:
                # Checking if Target belongs to the right Portion:
                if nums[r]>= target > nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
            else:
            # At this point whole of the values between left index and mid index contains same value and duplicates so we just shift one pointer.
                l+=1
        return False


