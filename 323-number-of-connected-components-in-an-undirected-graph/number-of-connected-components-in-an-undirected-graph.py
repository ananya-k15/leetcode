class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjacencyList = {x: [] for x in range(n)}
        for u, v in edges:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)

        components = 0
        seen = set()

        for v in range(n):
            if v in seen:
                continue
            seen.add(v)
            stack = [v]
            while stack != []:
                u = stack.pop()
                for neighbour in adjacencyList[u]:
                    if neighbour not in seen:
                        seen.add(neighbour)
                        stack.append(neighbour)
            components += 1

        return components