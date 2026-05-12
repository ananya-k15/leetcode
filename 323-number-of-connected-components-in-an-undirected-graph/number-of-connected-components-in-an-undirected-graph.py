class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjacencyList = {x: [] for x in range(n)}
        for u, v in edges:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)

        stack = []
        components = 0
        seen = set()

        for v in range(n):
            if v in seen:
                continue
            stack.append(v)
            while stack != []:
                u = stack.pop()
                seen.add(u)
                for neighbour in adjacencyList[u]:
                    if neighbour not in seen:
                        stack.append(neighbour)
            components += 1

        return components