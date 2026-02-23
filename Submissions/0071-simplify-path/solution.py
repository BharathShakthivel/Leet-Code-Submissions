class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        x = path.split("/")
        for i in x:
            if i == "" or i ==".":
                continue
            if i == "..":
                if len(stack) !=0:
                    stack.pop()
            else:
                stack.append(i)
        return "/" + "/".join(stack)
