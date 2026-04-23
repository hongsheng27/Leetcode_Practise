class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stack = []
        for p in parts:
            if p == "" or p == ".":
                pass
            elif p == "..":
                if stack: stack.pop()
            else:
                stack.append(p)

        return "/" + "/".join(stack)
