class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Brute Force - DFS - TIME LIMIT EXCEEDED
        # Time complexity: O((V+E)∗ m); Space complexity: O(V+E+m)
        # from collections import defaultdict
        # pre_map = defaultdict(list)
        # answer = []
        # if not prerequisites:
        #     for j in range(numCourses):
        #         answer.append(False)
        #     return answer
        # for crs,pre in prerequisites:
        #     pre_map[crs].append(pre)
        
        # def dfs(crs,tar):
        #     if crs == tar:
        #         return True
        #     for neigh in pre_map[crs]:
        #         if dfs(neigh,tar):
        #             return True
        #     return False
        
        # for u,v in queries:
        #     answer.append(dfs(u,v))
        # return answer
        
        #  Optimal - DFS - Hashset - Running dfs and building hashset
        from collections import defaultdict
        pre_map = defaultdict(list)
        answer = []

        for pre,crs in prerequisites:
            pre_map[crs].append(pre)
        
        
        def dfs(crs):
            if crs not in prereq_map:
                prereq_map[crs] = set()
                for neigh in pre_map[crs]:
                    dfs(neigh)
                    prereq_map[crs] |= prereq_map[neigh]
                prereq_map[crs].add(crs)
            # return prereq_map[crs]
        prereq_map = {}
        for i in range(numCourses):
            dfs(i)
        
        for u,v in queries:
            answer.append(u in prereq_map[v])
        return answer
