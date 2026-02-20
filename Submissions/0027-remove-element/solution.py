class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # left = 0
        # right = len(nums) - 1

        # while left <= right:
        #     if nums[left] != val:
        #         left+=1
        #     elif nums[right] == val:
        #         right-=1
        #     else:
        #         nums[left],nums[right] = nums[right],nums[left]
        #         left+=1
        #         right-=1
        # return left

        # 'k' acts as a "write-pointer" to track the position of the next valid element.
        # It also serves as the count of elements not equal to 'val'.
        k = 0
        
        # 'i' is the "scan-pointer" that iterates through every element in the list.
        for i in range(len(nums)):
            # If the current element is NOT the one we want to remove:
            if nums[i] != val:
                # Copy the valid element to the 'k-th' index.
                # This effectively overwrites any 'val' instances found earlier.
                nums[k] = nums[i]
                
                # Move the write-pointer forward to the next available slot.
                k += 1
        
        # After the loop, the first 'k' elements contain all non-'val' numbers.
        return k
