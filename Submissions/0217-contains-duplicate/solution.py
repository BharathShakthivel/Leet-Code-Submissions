class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if len(set(nums)) == len(nums):
        #     return False
        # else:
        #     return True
        
        # Hashset approach Time - O(n) and Space - O(n)
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
        
