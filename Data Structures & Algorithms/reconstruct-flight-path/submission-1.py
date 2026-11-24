class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        G = defaultdict(list)

        for x, y in sorted(tickets, reverse=True):
            G[x].append(y)

        ans = []

        def dfs(node):
            while G[node]:
                i = G[node].pop()
                dfs(i)
            ans.append(node)
        dfs("JFK")

        return ans[::-1]