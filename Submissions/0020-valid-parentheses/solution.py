class Solution:
    def isValid(self, s: str) -> bool:
        # stack=[]
        # maps = {')':'(','}':'{',']':'['}
        # for i in s:
        #     if i in '([{':
        #         stack.append(i)
        #     elif i in ')]}':
        #         if not stack or stack.pop() != maps[i]:
        #             return False
        # return not stack





















        stack = []
        maps = {")":"(",
                "}":"{",
                "]":"[",}
        for i in s:
            if i in "[{(":
                stack.append(i)
            elif i in ")]}":
                if not stack or stack.pop(-1) != maps[i]:
                    return False
        return not stack

