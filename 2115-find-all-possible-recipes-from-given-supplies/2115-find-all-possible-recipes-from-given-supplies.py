class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        # build recipes => ingredients adj list
        # since the point is not idendity cycle, is to find if can make recipes, I think bfs + indegree is better
        # put value to queue which indegree = 0 and include in supplies
        receipSet = set(recipes)
        supplieSet = set(supplies)
        indegree = defaultdict(int)
        adj = defaultdict(list)
        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                receipt = recipes[i]
                ingredient = ingredients[i][j]
                indegree[ingredient]
                indegree[receipt] += 1
                adj[ingredients[i][j]].append(recipes[i])
        q = deque(supplies)
        res = []
        while q:
            item = q.popleft()
            if item in receipSet: res.append(item)
            for nei in adj[item]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res


        