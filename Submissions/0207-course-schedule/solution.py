class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        from collections import defaultdict
        d = defaultdict(list)
        for crs,pre in prerequisites:
            d[crs].append(pre)
        
        def dfs(crs):
            if crs in visit:
                return False
            if d[crs] == []:
                return True
            visit.add(crs)
            for pres in d[crs]:
                if not dfs(pres): return False
            visit.remove(crs)
            d[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True


