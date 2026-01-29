class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #FAILED TRY
        
        # stack =[]
        # for i,a in enumerate(asteroids):
        #     if a > 0:
        #         stack.append(a)
        #     temp = a
        #     while stack and temp+stack[-1]<=0:
        #         current_stack_value = stack.pop()
        #         temp+=current_stack_value
        #     if temp<0:
        #         stack.pop()
        #         stack.append(a)
        # return stack

    #WORKING LOGIC

        '''
        Your logic should follow this shape:

            For each asteroid:
            Assume asteroid is alive
                While collision possible: (If stack is not empty and top stack > 0 and current value < 0)
                    If stack bigger:
                        Current dies
                        Stop loop (break)
                    If current bigger:
                        Pop stack
                        Continue loop
                    If equal:
                        Pop stack
                        Current dies
                    Stop loop
                After loop:
                    If current still alive:
                        Append to stack
            Return Final Stack
        '''

        stack = []
        for a in asteroids:
            alive = True
            while stack and stack[-1]>0 and a<0:
                # Step 1
                if abs(stack[-1])>abs(a):
                    alive = False
                    break
                 # Step 2
                elif abs(a) > abs(stack[-1]):
                    stack.pop()
                    continue
                elif abs(a) == abs(stack[-1]):
                    stack.pop()
                    alive = False
                    break
            if alive: 
                stack.append(a)
        return stack

            
            

