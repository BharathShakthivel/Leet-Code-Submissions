class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "C":
                stack.pop()
            elif i == "D":
                stack.append(stack[-1]*2)
            elif i == "+":
                x = stack[-1]
                y = stack[-2]
                stack.append(x+y)
            else:
                stack.append(int(i))
                
        return sum(stack)
