class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Brute Force - O(nlog n)
        # nums.sort()
        # return nums[-k]

        # Using Max Heap
        max_heap = [-p for p in nums]
        heapq.heapify(max_heap)
        res = 0
        for i in range(k):
            res = heapq.heappop(max_heap)
        return -res

        # Using Quick sort - O(n) ; In worst case - O(n^2) - Test case 45 Failed - TLE

        # k = len(nums)-k
        # def quick_select(l,r):
        #     if l == r:
        #         return nums[l]
        #     p,pivot = l, nums[r]
        #     for i in range(l,r):
        #         if nums[i] < pivot:
        #             nums[p],nums[i] = nums[i],nums[p]
        #             p+=1
        #     nums[p],nums[r] = nums[r],nums[p]
        #     if p > k:
        #         return quick_select(l,p-1)
        #     elif p<k:
        #         return quick_select(p+1,r)
        #     else:
        #         return nums[p]
        # return quick_select(0, len(nums)-1)



