class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        out = nums1 + nums2
        out.sort()
        n = len(out)
        if n%2 == 0:
            index_1 = n//2 - 1
            index_2 = n//2 
            return (out[index_1]+out[index_2])/2
        else:
            return out[n//2]
