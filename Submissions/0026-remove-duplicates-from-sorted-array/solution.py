class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # write = 0
        # read = 1
        # while(read<=len(nums)-1):
        #      if nums[read]!=nums[write]:
        #         write+=1
        #         nums[write]=nums[read]
        #      else:
        #         pass
        #      read+=1
        # return write+1

        l = 1
        r = 1
        while r != len(nums):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
                r+=1
            else:
                r+=1
        return l


        # write_pointer = 0
        # read_pointer = 1
        # while(read_pointer<len(nums)):
        #     if nums[read_pointer]!= nums[write_pointer]:
        #         write_pointer+=1
        #         nums[write_pointer] = nums[read_pointer]
        #     else:
        #         pass
        #     read_pointer+=1
        # return write_pointer+1
