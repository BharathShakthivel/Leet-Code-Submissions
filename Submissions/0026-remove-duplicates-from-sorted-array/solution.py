class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        read = 1
        while(read<=len(nums)-1):
             if nums[read]!=nums[write]:
                write+=1
                nums[write]=nums[read]
             else:
                pass
             read+=1
        return write+1

