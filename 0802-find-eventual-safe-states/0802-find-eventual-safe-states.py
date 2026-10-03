class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        
        #First we reverse the given graph.
        V = len(graph)
        adj_list = [[] for _ in range(V)] 
        indegrees = [0 for _ in range(V)]
        for node in range(0, V):
            for adjnode in graph[node]:
                adj_list[adjnode].append(node)
                indegrees[node] += 1 #here we calculate indegrees

        queue = deque()

        #Add all the nodes with indegrees 0 in queue
        for node in range(0, V):
            if indegrees[node] == 0:
                queue.append(node)

        result = []
        while len(queue) != 0:
            curr_node = queue.popleft()
            result.append(curr_node)
            for adjnode in adj_list[curr_node]:
                indegrees[adjnode] -= 1
                if indegrees[adjnode] == 0:
                    queue.append(adjnode)

        result.sort()
        return result

