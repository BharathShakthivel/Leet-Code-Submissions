class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # my_dict = {}
        # res = []
        # for i in nums:
        #     if i not in my_dict:
        #         my_dict[i]=1
        #     else:
        #         my_dict[i]+=1

        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)
        res = []

        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
