class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        OPTIMAL PATTERN

        # 1. CHARACTER MAPS: Create frequency maps for s1 and the current window.
        #    Since we only care about lowercase letters, max size is 26 (O(1) space).

        # 2. SLIDING THE WINDOW:
        #    - Use a 'right' pointer (r) to expand the window by adding s2[r].
        #    - Check if the window size (r - l + 1) exceeds the target size (len(s1)).

        # 3. MAINTAINING WINDOW SIZE (The "Caterpillar" Step):
        #    - If too large, remove s2[l] from the window map.
        #    - IMPORTANT: In Python, delete the key if count hits 0 to keep dicts comparable.
        #    - Increment the 'left' pointer (l) to slide the window forward.

        # 4. THE COMPARISON:
        #    - Once the window is exactly the right size, compare s1_map and window_map.
        #    - If they match, you found a permutation! Return True.

        # 5. FALLBACK:
        #    - If the loop finishes without a match, return False.

        #Edge case: When the length of S1 string greater than S2, we simply return False (We check this at start)

        '''
        
        
        
        
        # Brute Force:
        # s1 = sorted(s1)
        # for i in range(len(s2)):
        #     for j in range(i,len(s2)):
        #         sub_string = s2[i:j+1]
        #         sub_string = sorted(sub_string)
        #         if sub_string == s1:
        #             return True
        # return False   
        
        # O(N) Approach
        
        if len(s1) > len(s2):
            return False
        s1_dict = {}
        s2_dict = {}
        for i in range(len(s1)):
            s1_dict[s1[i]] = 1 + s1_dict.get(s1[i],0)
        l = 0
        for r in range(len(s2)):
            s2_dict[s2[r]] = 1 + s2_dict.get(s2[r],0)
            length = r - l + 1
            if length > len(s1):
                if s2_dict[s2[l]] == 1:
                    s2_dict.pop(s2[l])
                else:
                    s2_dict[s2[l]] -= 1
                l+=1
            if s1_dict == s2_dict:
                return True
        return False


        # O ( 26 * n) - Hashmap Approach

        

