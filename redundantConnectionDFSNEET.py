class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(node, target, visited):
            if node == target:
                return True
            
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True
            return False
        
        for i, j in edges:
            if i in graph and j in graph:
                visited = set()
                if dfs(i, j, visisted):
                    return [i, j]
                
            if i not in graph:
                graph[i] = []
            if j not in graph:
                graph[j] = []

            graph[i].append(j)
            graph[j].append(i)

        return []