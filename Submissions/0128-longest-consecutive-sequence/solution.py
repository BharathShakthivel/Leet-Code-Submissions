class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      nums = set(nums)
      res = 0
      for i in nums:
        if i - 1 not in nums:
            count = 1
            while i + 1 in nums:
                count+=1
                i+=1
            if count > res:
                res = count
      return res  
