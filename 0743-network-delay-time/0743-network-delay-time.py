class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        #Bellman ford algorithm

        dist = [float("inf") for _ in range(n + 1)]
        dist[k] = 0

        for _ in range(n - 1):
            for u,v,w in times:
                if dist[u] != float("inf"):
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

        if float("inf") in dist[1:]: #here we are checking if all the nodes receives the signal or not if any one of the node is not receive we return -1.
            return -1
        
        return max(dist[1:]) #we are using slicing to ignore the 0th node in dist.
