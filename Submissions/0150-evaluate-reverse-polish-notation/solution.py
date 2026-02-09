class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        valid_operators = {'+','-','*','/'}
        stack = []
        def operations(operation,a,b):
            if operation == '+':
                answer = a + b
                return answer
            elif operation == '-':
                answer = a - b
                return answer
            elif operation == '*':
                answer = a * b
                return answer
            else:
                if b == 0:
                    return -1
                else:
                    answer = a / b
                    return answer

        for token in tokens:
            if token not in valid_operators:
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(operations(token,int(a),int(b)))
        return int(stack[-1])

