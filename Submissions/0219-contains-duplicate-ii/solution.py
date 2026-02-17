class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        🧠 Memorize the Pattern (Important)
        1.We need to check duplicates within distance k
        2.That means we only care about the last k elements
        3.Use a sliding window of size k
        4.Use a set for fast duplicate checking
        5.If window size > k → remove left element
        6.If current element already in set → return True
        '''
             
        # Step 1: Use a set to maintain a sliding window of at most k elements
        # The set helps us check duplicates in O(1) time
        window = set()
        
        # Step 2: Left pointer of the sliding window
        l = 0
        
        # Step 3: Iterate with right pointer
        for r in range(len(nums)):
            
            # Step 4: If window size exceeds k,
            # remove the leftmost element and shrink window
            if r - l > k:
                window.remove(nums[l])
                l += 1
            
            # Step 5: If current number already exists in window,
            # we found a duplicate within distance k
            if nums[r] in window:
                return True
            
            # Step 6: Add current element to window
            window.add(nums[r])
        
        # Step 7: No duplicates found within distance k
        return False
