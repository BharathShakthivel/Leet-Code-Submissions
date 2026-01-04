class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #    i = m -1 
    #    j = n -1 
    #    k = m + n -1
    #    while j >= 0:
    #     if i>=0 and nums1[i] > nums2[j]:
    #         nums1[k] = nums1[i]
    #         i-=1
    #     else:  
    #         nums1[k] = nums2[j]
    #         j-=1
    #     k-=1

        if n == 0 :return
        len1 = len(nums1)
        end_idx = len1-1
        while n > 0 and m > 0 :
            if nums2[n-1] >= nums1[m-1]:
                nums1[end_idx] = nums2[n-1]
                n-=1
            else:
                nums1[end_idx] = nums1[m-1]
                m-=1
            end_idx-=1
        while n > 0:
            nums1[end_idx] = nums2[n-1]
            n-=1
            end_idx-=1
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
