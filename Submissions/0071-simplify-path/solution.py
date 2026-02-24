class Solution:
    def simplifyPath(self, path: str) -> str:
        
        """
        # 1. Split the path by "/"
        # 2. Create an empty stack
        # 3. For each part:
        #       - If "" or "."  → ignore
        #       - If ".."       → pop from stack (if not empty)
        #       - Else          → push folder name to stack
        # 4. Join stack with "/" and add leading "/"
        # 5. Return result

        """
        





        
        
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
