class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # We preserve the original index
        #  We will use enumerate function to get the index as well as the value.
        for index,task in enumerate(tasks):
            task.append(index)
        # We sort the task based on the enque time.
        tasks.sort(key = lambda t : t[0])
        #  We initialise certain variables to calculate the time and store our indexed results
        result,time,i,min_Heap = [],tasks[0][0],0,[]

        while min_Heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(min_Heap,[tasks[i][1],tasks[i][2]])
                i+=1
            if not min_Heap:
                time = tasks[i][0]
            else:
                processing_time,original_index = heapq.heappop(min_Heap)
                time+=processing_time
                result.append(original_index)
        return result



