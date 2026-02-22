class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        Logic - Binary Search:
        Instead of searching for elements, search for the starting index l of the $k$-length window. 
        The possible start range is [0, n-k]. 
        For a candidate mid, compare the element at mid with the element just outside the window at mid + k. 
        If mid is further from $x$ than mid + k, the optimal window must start further to the right.
        '''

        # Binary Search - O(log (n-k)+k)

        l = 0
        r = len(arr)-k
        while l<r:
            mid = (l+r)//2
            if x- arr[mid] > arr[mid+k] -x:
                l = mid+1
            else:
                r = mid
        return arr[l:l+k]
        
        
        # Two Pointer - O(n) Time and O(1) Space

        '''
        Logic - Two pointer :
        Start with the widest possible window (the entire array). 
        Compare the distances of the two ends from x. Discard the element that is further away. 
        If distances are tied, discard the right element to favor the smaller value. 
        Repeat until the window size is exactly k.

        Working Example: arr = [1, 2, 3, 4, 5], k = 2, x = 3
        Initial: [1, 2, 3, 4, 5], l=0, r=4. Window size is 5 (> 2).
        Step 1: |1-3| = 2, |5-3| = 2. It's a tie! Move r down.
            l=0, r=3. Array: [1, 2, 3, 4]
        Step 2: |1-3| = 2$, |4-3| = 1. 1 is further than 4. Move l up.
            l=1, r=3. Array: [2, 3, 4]
        Step 3: |2-3| = 1, |4-3| = 1. Tie! Move r down.
            l=1, r=2. Array: [2, 3]
        End: Window size is 2. Return [2, 3].
        
        '''
        # l = 0
        # r = len(arr)-1
        # while r-l+1 > k:
        #     if x - arr[l] > arr[r]-x:
        #         l+=1
        #     else:
        #         r-=1
        # return arr[l:r+1]



