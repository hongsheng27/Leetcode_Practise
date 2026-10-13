class Node:
    def __init__(self, name):
        self.name = name # 0 unsure, 1 group1, -1 group2
        self.group = 0

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        # check if graph[u] is all in one set, u in different set
        # {0} {1, 2, 3}
        # {1} {0, 2}
        # traverse graph, union find to check if reach the condition
        # 12:15
        # traverse, 1 => group 2 groups, -1 => group 2, if contradict than return False
        n = len(graph)
        nodes = {i: Node(i) for i in range(n)}

        for i in range(n):
            if nodes[i].group == 0: 
                nodes[i].group = 1
                q = deque([i])

                while q:
                    elem = q.popleft()
                    for other in graph[elem]:
                        if nodes[other].group == 0:
                            nodes[other].group = -nodes[elem].group
                            q.append(other)
                        elif nodes[other].group == nodes[elem].group: 
                            return False
                        
        return True