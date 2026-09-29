class Solution:
    def dfs(self, curr_node, visited, graph, color):
        visited[curr_node] = color

        for adjnode in graph[curr_node]:
            if visited[adjnode] != -1: #eska matlab uss koi color given hai(0,1)
                if visited[adjnode] == color:
                    return False

            else:
                ans = self.dfs(adjnode, visited, graph, 1 - color)
                if ans == False:
                    return False
                    
        return True

    def isBipartite(self, graph: list[list[int]]) -> bool:
        total_nodes = len(graph)
        visited = [-1] * total_nodes

        #For connected components
        for index in range(0, total_nodes):
            if visited[index] == -1:
                ans = self.dfs(index, visited, graph, 0)
                if ans == False:
                    return False

        return True
