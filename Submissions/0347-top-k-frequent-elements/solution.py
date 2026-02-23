class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # count = {}
        # freq = [[] for i in range(len(nums)+1)]

        # for n in nums:
        #     count[n] = 1 + count.get(n,0)
        # for n, c in count.items():
        #     freq[c].append(n)
        # res = []

        # for i in range(len(freq)-1,0,-1):
        #     for j in freq[i]:
        #         res.append(j)
        #         if len(res) == k:
        #             return res

         #We are using Bucket Sorting ALgorithm
        #We need to count the frequency of the element using the HashMap
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        # We are creating the list within the list to put the elements which corresponds to size of the array. Let us say if the array has size 5 and all the values in the original nums array, our freq list would be having all the distinct items in the inner list of the index 4 of the outer list.

        # Now we loop through the count,
        for n in nums:
            count[n] = 1 + count.get(n,0)
        # we access the number and it's frequency using the key value pair by the .items method
        for n ,c in count.items():
        # We append it to the inner list of count corresponding to its's index(frequency of the elements)which is nothing but the frequency compared to size of the input array. 

        # WE DO THIS METHOD IN ORDER TO ACHIEVE BIG O(N)

            freq[c].append(n)
        
        # We take extra space to obtain the top most k elements and we keep it as a list.
        res = []

        # We loop through the count from decending order meaning, from the backwards,
        # We also loop through the inner list to get access of the top most frequent k elements.
        # We keep appending those elements to our list.
        # We check if the results size of the result matches k then we return the list and that would be the answer for the top most frequent k elements.
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
