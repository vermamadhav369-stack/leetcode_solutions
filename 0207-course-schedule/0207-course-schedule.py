class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # in this we are using topological sort. 
        adj_list = [[] for _ in range(numCourses)]
        indegrees =[0 for _ in range(numCourses)]
        
        for u, v in prerequisites:
            adj_list[u].append(v)
            indegrees[v] += 1
            
        queue = deque()
        result = []
        
        for i in range(0, numCourses):
            if indegrees[i] == 0:
                queue.append(i)
                
        while len(queue) != 0:
            curr_node = queue.popleft()
            result.append(curr_node)
            for adjnode in adj_list[curr_node]:
                indegrees[adjnode] -= 1
                if indegrees[adjnode] == 0:
                    queue.append(adjnode)
        
        if len(result) == numCourses:
            return True
        return False