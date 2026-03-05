class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Brute Force Time - (O(N)); Space - (O(N)) 
        # hash = set()
        # for i in nums:
        #     if i in hash:
        #         return i
        #     hash.add(i)
        
        # Optimal Solution
        
        # SLow and FAst Pointer - Flyods's algorithm; Linked LIst Pattern
        # We find the cycle point using slow and fast pointer technique
        # Then initialise another pointer from start and move the 
        # current slow pointer and eventually they will meet at a point which is the guarenteed duplicate value.

        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow== fast:
                break
        slow_2 = 0
        while True:
            slow_2 = nums[slow_2]
            slow = nums[slow]
            if slow == slow_2:
                return slow
