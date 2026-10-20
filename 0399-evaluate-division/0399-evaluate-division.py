class Variable:
    def __init__(self, name):
        self.name = name
        self.neis = []
        self.weight = 0
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build a graph with weight i.g. Class a, neis = [(b, 2.0)] 
        # use a map to find Variable
        # use queries to change a = weight * c, than caluclate
        # 2: 00
        variableMap = {}
        for u, v in zip(equations, values):
            first = Variable(u[0]) if u[0] not in variableMap else variableMap[u[0]]
            second = Variable(u[1]) if u[1] not in variableMap else variableMap[u[1]]
            first.neis.append((second.name, v))
            second.neis.append((first.name, 1 / v))
            variableMap[first.name] = first
            variableMap[second.name] = second
        visited = set()
        def dfs(variable, destination):
            if variable not in variableMap or destination not in variableMap: return -1
            if variable == destination: return 1
            visited.add(variable)
            for (nei, w) in variableMap[variable].neis:
                if nei in visited: continue
                product = dfs(nei, destination) 
                if product != -1:
                    visited.clear()
                    return product * w
            visited.remove(variable)
            return -1
        res = []
        for first, second in queries:
            res.append(dfs(first, second))
        return res
        # 32: 45 debug
        # infinite loop => need visited
        # edge case => x, y not exist in graph
        # 36:16 ai debug
        # first = Variable(u[0])
        # second = Variable(u[1]), every time create new Node