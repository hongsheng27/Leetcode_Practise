class Node:
    def __init__(self, name):
        self.name = name
        self.neis = []
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build a graph with weight i.g. Class a, neis = [(b, 2.0)] 
        # use a map to find Variable
        # use queries to change a = weight * c, than caluclate
        nodes = {}
        for u, v in zip(equations, values):
            first, second = u
            if first not in nodes:
                nodes[first] = Node(first)
            if second not in nodes:
                nodes[second] = Node(second)
            nodes[first].neis.append((second, v))
            nodes[second].neis.append((first, 1 / v))
    
        def dfs(node, target, visited):
            if node not in nodes or target not in nodes: return -1
            if node == target: return 1.0
            visited.add(node)
            for (nei, w) in nodes[node].neis:
                if nei in visited: continue
                product = dfs(nei, target, visited) 
                if product != -1.0:
                    visited.remove(node)
                    return product * w
            return -1.0

        res = []
        for start, end in queries:
            res.append(dfs(start, end, set()))
        return res