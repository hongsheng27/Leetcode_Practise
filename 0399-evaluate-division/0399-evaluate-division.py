class Node:
    def __init__(self, name):
        self.name = name
        self.neis = []


class Solution:
    def calcEquation(self, equations, values, queries):
        nodes = {}

        for (a, b), value in zip(equations, values):
            if a not in nodes:
                nodes[a] = Node(a)
            if b not in nodes:
                nodes[b] = Node(b)

            nodes[a].neis.append((nodes[b], value))
            nodes[b].neis.append((nodes[a], 1 / value))

        def dfs(node, target, product, visited):
            if node.name == target:
                return product

            visited.add(node.name)

            for nei, weight in node.neis:
                if nei.name not in visited:
                    result = dfs(
                        nei,
                        target,
                        product * weight,
                        visited
                    )

                    if result != -1:
                        return result

            return -1

        res = []

        for start, end in queries:
            if start not in nodes or end not in nodes:
                res.append(-1.0)
            else:
                res.append(
                    dfs(nodes[start], end, 1.0, set())
                )

        return res