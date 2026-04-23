class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stack = []
        print(parts)
        for p in parts:
            alive = True
            if p == "":
                alive = False
            elif stack and p == "..":
                stack.pop()
                alive = False
            elif p == ".." or p == ".":
                alive = False
            if alive: stack.append(p)

        return "/" + "/".join(stack)
