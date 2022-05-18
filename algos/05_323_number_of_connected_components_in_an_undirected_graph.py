# "Incorrect" solution. This solution finds the number of connected components. The problem specifically requires the number of connected components from node 0 to node n.
# Confused about "n nodes" beyond half test cases therefore skipping.

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}

        for edge in edges:
            src, dest = edge
            if src in graph:
                graph[src].append(dest)
            else:
                graph[src] = [dest]

        visited = set()
        res = 0
        for src in graph.keys():
            if src not in visited:
                self.dfs(graph, src, visited)
                res += 1

        return res

    def dfs(self, graph, src, visited):
        if src in visited:
            return
        visited.add(src)
        if src not in graph:
            return
        for dest in graph[src]:
            self.dfs(graph, dest, visited)