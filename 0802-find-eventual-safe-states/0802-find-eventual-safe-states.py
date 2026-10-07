class Solution:
    def dfs(self, curr_node, graph, visited, path_visited, is_safe):
        visited[curr_node] = 1
        path_visited[curr_node] = 1

        for adjnode in graph[curr_node]:
            if visited[adjnode] == 0:
                ans = self.dfs(adjnode, graph, visited, path_visited, is_safe)
                if ans == False:
                    return False

            elif path_visited[adjnode] == 1:
                return False

        path_visited[curr_node] = 0
        is_safe[curr_node] = 1
        return True

    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        V = len(graph)
        visited = [0 for _ in range(V)]
        path_visited = [0 for _ in range(V)]
        is_safe = [0 for _ in range(V)]

        for i in range(0,V):
            if visited[i] == 0:
                self.dfs(i, graph, visited, path_visited, is_safe)

        result = []
        for i in range(V):
            if is_safe[i] == 1:
                result.append(i)

        return result
