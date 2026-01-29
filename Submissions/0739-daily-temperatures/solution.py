class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute Force O(N2) - Not working
        # out = [0] * len(temperatures)
        # for j in range(len(temperatures)):
        #     for k in range(j+1,len(temperatures)):
        #         if temperatures[k] > temperatures[j]:
        #             out[j] = (k+1)-(j+1)
        #             break
        # return out

        # Optimised Solution - Monotonic Stack, we iterate through the temperatures one time and finish this in O(n) time and with extra space (stack)(O(n))
        res = [0] * len(temperatures)
        stack = [] # pair (temp,index)
        for i,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_temp,stack_index = stack.pop()
                res[stack_index] = i - stack_index # current index(warmer temp) - stack_index
            stack.append((t,i))
        return res
