class Solution:
    #Floyd Warshall
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        matrix = [[float("inf") for _ in range(n)] for _ in range(n)]

        for u,v,w in edges:
            matrix[u][v] = w
            matrix[v][u] = w

        for i in range(n): #har node ka apne aap se distance (0) hoga.
            matrix[i][i] = 0

        #for finding the shortest distance of all nodes to all other nodes.
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][via] != float("inf") and matrix[via][j] != float("inf"):
                        matrix[i][j] = min(matrix[i][j],matrix[i][via] + matrix[via][j])                                        

        #esme ham har city se jitne neighbors reachable hai vo count kar rahe hai.
        result = []
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and matrix[i][j] <= distanceThreshold: #current city ko khud count nehi karna[i != j] bas unko karna hai jinka S.D, distanceThreshold ke andar aur equal hai
                    count += 1
            result.append([i,count])

        #here we are finding the smallest number of cities that are reachable
        min_count = float("inf")
        city = -1
        for i, count in result:
            if count <= min_count:
                min_count = count
                city = i

        return city
                        
        