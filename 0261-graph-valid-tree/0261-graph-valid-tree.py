class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # Connected：所有 nodes 必須連通
        # Acyclic：不能存在 cycle
        
        # edge should be == V - 1
        # start from any node
        # len visited should be equal to node len
        if len(edges) != n - 1: return False
        adj = defaultdict(list)
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        visited = set([0])
        q = deque([0])
        
        while q:
            elem = q.popleft()
            for nei in adj[elem]:
                if nei not in visited: 
                    visited.add(nei)
                    q.append(nei)
        return len(visited) == n
      