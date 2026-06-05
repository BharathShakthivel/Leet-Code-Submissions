class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        minHeap = []
        count = {}
        for i in hand:
            count[i] = 1 + count.get(i,0)
        for key in count.keys():
            heapq.heappush(minHeap, key)
        
        while minHeap:
            first = minHeap[0]
            for i in range(first, first+groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True


