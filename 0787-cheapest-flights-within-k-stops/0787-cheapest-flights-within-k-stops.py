class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for u,v,cost in flights:
            adj_list[u].append([v,cost])

        min_cost = [float("inf") for _ in range(n)]
        min_cost[src] = 0

        queue = deque()
        queue.append([0,src,0]) #step,node,cost

        while len(queue) != 0:
            step, node, cost = queue.popleft()

            for adjnode,curr_cost in adj_list[node]:
                new_cost = cost + curr_cost

                if new_cost < min_cost[adjnode]:
                    new_step = step + 1
                    
                    if new_step == k + 1:
                        if adjnode != dst:
                            continue

                    min_cost[adjnode] = new_cost
                    queue.append([new_step,adjnode,new_cost])

        if min_cost[dst] == float("inf"):
            return -1

        return min_cost[dst]
