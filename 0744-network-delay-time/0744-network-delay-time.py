class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i + 1: [] for i in range(n)}
        for src, targ, cost in times:
            adj[src].append((cost, targ))

        heap = [(0, k)]
        visited = set()
        res = 0

        while heap:
            curCost, cur = heapq.heappop(heap)
            if cur not in visited:
                visited.add(cur)
                res = max(res, curCost)
                for cost, nei in adj[cur]:
                    if nei not in visited:
                        heapq.heappush(heap, (cost + curCost, nei))
            


        return res if len(visited) == n else -1
        