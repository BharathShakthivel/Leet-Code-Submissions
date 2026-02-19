class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        (Pattern)
        Expand right
        Update freq
        Update maxFreq
        If invalid → shrink left
        Update result

        '''
        # Pattern: Optimized Sliding Window

        # Step 1: Initialize:
        #         l = 0
        #         hashmap = {}
        #         maxFreq = 0
        #         res = 0
        # Step 2: Expand window by moving r.
        #         Add s[r] to hashmap.
        # Step 3: Update maxFreq:
        #         maxFreq = max(maxFreq, hashmap[s[r]])
        # Step 4: Calculate window_size = r - l + 1
        # Step 5: If replacements needed:
        #         window_size - maxFreq > k
        #         → window invalid
        #         → shrink window from left
        #             decrease hashmap[s[l]]
        #             move l forward
        # Step 6: Update result:
        #         res = max(res, window_size)
        # Step 7: Return res
        
        # EvenBetter Approach
        # hashmap = {}
        # l = 0
        # res = 0
        # max_freq = 0
        # for r in range(len(s)):
        #     hashmap[s[r]] = 1 + hashmap.get(s[r],0)
        #     window_length = r - l + 1
        #     max_freq = max(max_freq,hashmap[s[r]])

        #     while window_length - max_freq > k:
        #             hashmap[s[l]] -= 1
        #             l+=1
        #             window_length = r - l +1
        #     res = max(res,window_length)
        # return res       
        


        # Pattern: Sliding Window + Frequency Map

        # Step 1: Use two pointers (l, r) to maintain a window.
        # Step 2: Use hashmap to count frequency of characters inside window.
        # Step 3: Expand window by moving r.
        #         Add s[r] into hashmap.
        # Step 4: Calculate:
        #         window_size = r - l + 1
        #         maxFreq = max(hashmap.values())
        # Step 5: Check if replacements needed:
        #         window_size - maxFreq > k
        #         If yes → window invalid → shrink from left.
        # Step 6: While invalid:
        #             decrease frequency of s[l]
        #             move l forward
        # Step 7: Update result with max window length seen so far.
        # Step 8: Return result.

        # Better Approach - O(26) * n
        hashmap = {}
        l = 0
        res = 0
        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r],0)
            length = r - l + 1
            while length - max(hashmap.values()) > k:
                    hashmap[s[l]] -= 1
                    l+=1
                    length = r - l +1
            res = max(length,res)
        return res
        
        
# -----------------------------------------------------------------------------------------------------------


        # Failed Approach
        
        # l = 0
        # res = s[l]
        # window = set()
        # if len(s) == l:
        #     return 0
        # for r in range(1,len(s)):
        #     if s[r] in window:
        #         res+=s[l]
        #         window.add(s[r])
        #         continue
        #     if s[r] not in window:
        #         if k <=0 and r == len(s)-1:
        #             return len(res)
        #         else:
        #             res+=s[l]
        #             k-=1
        # return len(res)
            
