class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        vertices = {str(point): i + 1 for i, point in enumerate(points)}
        edges = []
        for i, [x_i, y_i] in enumerate(points):
            for [x_j, y_j] in points[i + 1:]:
                heapq.heappush(edges, (abs(x_i - x_j) + abs(y_i - y_j), vertices[str([x_i, y_i])], vertices[str([x_j, y_j])]))

        par = [i for i in range(len(points) + 1)]
        rank = [1] * (len(points) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        # return False if already unioned
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        cost = 0

        while edges:
            dist, a, b = heapq.heappop(edges)
            if union(a, b):
                cost += dist
            
        
        return cost
