class Node:
    def __init__(self, email):
        self.email = email
        self.neis = [] # Node
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # important: sorted order, idendity same person
        # union find: build j <= smith, newtwork, j <= smith, 00 structure, 
        nodes = {} # email: emailNode
        for account in accounts:
            owner, *rest = account
            first = rest[0]
            nodes[first] = Node(first) if first not in nodes else nodes[first]
            nodes[first].owner = owner
            for email in rest[1:]:
                nodes[email] = Node(email) if email not in nodes else nodes[email]
                nodes[email].owner = owner
                nodes[first].neis.append(nodes[email])
                nodes[email].neis.append(nodes[first])
        visited = set()
        def dfs(node, emails):
            visited.add(node)
            emails.append(node.email)
            for nei in node.neis:
                if nei in visited: continue
                dfs(nei, emails)

        res = []
        for node in nodes.values():
            if node not in visited:
                emails = []
                dfs(node, emails)
                res.append([node.owner] + sorted(emails))
        return res
            
            


            