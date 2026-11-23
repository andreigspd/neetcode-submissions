class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            G[x].append(y)
        
        vis = set()
        vis_current = set()
        loop = False
        def dfs(i):
            nonlocal loop
            vis.add(i)
            vis_current.add(i)
            for x in G[i]:
                if x in vis_current:
                    loop = True
                    return
                if x not in vis:
                    dfs(x)
            vis_current.remove(i)

        for i in range(numCourses):
            if i not in vis:
                vis_current.clear()
                dfs(i)

        return not loop
