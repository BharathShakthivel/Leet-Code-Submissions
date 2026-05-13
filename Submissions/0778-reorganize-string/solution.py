class Solution:
    def reorganizeString(self, s: str) -> str:

        freq_dict = {}
        res = ""
        max_heap = []

        for i in s:
            freq_dict[i] = 1 + freq_dict.get(i,0)
        for k,v in freq_dict.items():
            heapq.heappush(max_heap,(-v,k))
        prev = None
        while max_heap or prev:
            if prev and not max_heap:
                return ""
            cnt,char = heapq.heappop(max_heap)
            res+=char
            cnt+=1
            if prev:
                heapq.heappush(max_heap,prev)
                prev = None
            if cnt !=0:
                prev = (cnt,char)
        return res


