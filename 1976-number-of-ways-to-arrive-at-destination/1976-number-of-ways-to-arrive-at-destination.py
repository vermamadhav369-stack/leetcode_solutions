class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        MOD = 10 ** 9 + 7

        adj_list = [[] for _ in range(n)]
        for u,v,w in roads:
            adj_list[u].append([v,w])
            adj_list[v].append([u,w])

        distance = [float("inf") for _ in range(n)]
        ways = [0 for _ in range(n)]

        distance[0] = 0
        ways[0] = 1

        priority_queue = [[0,0]] #distance,node

        while len(priority_queue) != 0:
            dist, node = heapq.heappop(priority_queue)
            for adjnode,d in adj_list[node]:
                new_dist = dist + d
                if new_dist < distance[adjnode]:
                    distance[adjnode] = new_dist
                    heapq.heappush(priority_queue,[new_dist, adjnode])
                    ways[adjnode] = ways[node]

                elif new_dist == distance[adjnode]:
                    ways[adjnode] += ways[node]

        return ways[n - 1] % MOD
        