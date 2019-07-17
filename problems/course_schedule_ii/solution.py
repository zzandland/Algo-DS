class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for prereq in prerequisites:
            adj[prereq[0]].append(prereq[1])
        visit = [-1] * numCourses
        output = []
        def helper(cur: int) -> bool:
            if visit[cur] == 0:
                return False
            visit[cur] = 0
            for ad in adj[cur]:
                if visit[ad] != 1:
                    if not helper(ad):
                        return False
            visit[cur] = 1        
            output.append(cur)
            return True
        for i in range(numCourses):
            if visit[i] == -1:
                if not adj[i]:
                    output.append(i)
                    visit[i] = 1
                else:
                    if not helper(i):
                        return []    
        return output                    