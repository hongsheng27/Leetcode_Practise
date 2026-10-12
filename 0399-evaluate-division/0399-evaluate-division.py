class Node:
    def __init__(self, name):
        self.name = name
        self.neis = [] # (node, weight)

class Solution:
    def calcEquation(self, equations, values, queries):
        nodes = {}
        for i, equation in enumerate(equations):
            first, second = equation
            if first not in nodes:
                nodes[first] = Node(first)
            if second not in nodes:
                nodes[second] = Node(second)
            nodes[first].neis.append((nodes[second], values[i]))
            nodes[second].neis.append((nodes[first], 1 / values[i]))
        def dfs(node, target, product, visited):
            if not node: return -1
            if node == target:
                return product
            visited.add(node)
            for nei, w in node.neis:
                if nei not in visited:
                    res = dfs(nei, target, product * w, visited)
                    if res != -1: return res
            visited.remove(node)
            return -1
        res = []
        for start, end in queries:
            if start in nodes and end in nodes:
                res.append(dfs(nodes[start], nodes[end], 1.0, set()))
            else:
                res.append(-1)
        return res