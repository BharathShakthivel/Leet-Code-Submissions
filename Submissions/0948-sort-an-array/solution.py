class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # # Brute Force
        # nums.sort()
        # return nums
        
        # Worst case solution - Selection Sort

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             pass
        #         elif nums[i]>nums[j]:
        #             nums[i],nums[j]=nums[j],nums[i]
        # return nums

        # Worst case solution - Bubble Sort
            # i = 0
            # n = len(nums)
            # while i != n-1:
            #     swapped = False
            #     for j in range(n-1-i):
            #         if nums[j] > nums[j+1]:
            #             nums[j],nums[j+1] = nums[j+1],nums[j]
            #             swapped = True
            #     if not swapped:
            #         break
            #     i+=1
            # return nums
        
        
        # #Optimal Solution -  Time & Space - n logn

        # #We will use merge sort
        # # We will use divide and conquer (This will done in log n times because n/2 pow(x) = 1)
        # # We split the array in 2 halves and merge the halves and overwrite in the passed array (Merging in done n sized array in one pass)
        # # So the entire solution is ( n log n )
        #         l,r = 0, len(nums)-1

        # # Merging the two halves
        # # We use this helper function
        # # We use three pointers
        #         def merge(arr,L,M,R):

        # #We take copies of the array in 2 halves
        #             left,right = arr[L:M+1],arr[M+1:R+1] # In python while slicing thelast element is not included
        # # We initialise three pointers
        #             i,j,k = L,0,0
        # # We check if the both the pointers reach till end of the array if theey are equal in size.
        #             while j<len(left) and k <len(right):
        #                 if left[j] > right[k]:
        #                     arr[i] = right[k]
        #                     k+=1
        #                 else:
        #                     arr[i] = left[j]
        #                     j+=1
        #                 i+=1
        # # We check if the both the pointers reach till end of the array if they are not equal in size, we just simply       
        #             while j< len(left):
        #                 arr[i] = left[j]
        #                 j+=1
        #                 i+=1
        #             while k< len(right):
        #                 arr[i] = right[k]
        #                 k+=1
        #                 i+=1

        # # We initialise l,r pointers
                        
        #         def merge_sort(arr,l,r):
        # # We first check if the left and right pointers are equal, we simply return the array cause we can't sort it, 
        # # it is already sorted
        #             if l  == r:
        #                 return arr
        #             m = (l + r) // 2
        #             merge_sort(nums,l,m)
        #             merge_sort(nums,m+1,r)
        #             merge(nums,l,m,r)
        #             return arr
        #         return merge_sort(nums,0,len(nums)-1)

        # # We use divide and conquer technique we pass in 2 poniters
















        def merge(arr,L,M,R):
            i,j,k = L,0,0
            LEFT = arr[L:M+1]
            RIGHT = arr[M+1:R+1]
            while j < len(LEFT) and k < len(RIGHT):
                if LEFT[j]> RIGHT[k]:
                    arr[i] = RIGHT[k]
                    k+=1
                else:
                    arr[i] = LEFT[j]
                    j+=1
                i+=1
            while j < len(LEFT):
                arr[i] = LEFT[j]
                i+=1
                j+=1
            while k < len(RIGHT):
                arr[i] = RIGHT[k]
                i+=1
                k+=1


        def merge_sort(arr,l,r):
            if l == r:
                return arr
            m = (l + r) // 2
            merge_sort(arr,l,m)
            merge_sort(arr,m+1,r)
            merge(arr,l,m,r)
            return arr
        return merge_sort(nums,0,len(nums)-1)
