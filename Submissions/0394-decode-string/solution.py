class Solution:
    def decodeString(self, s: str) -> str:
        import re
        stack =[]
        cur_string = ""
        cur_num = 0
        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            elif ch == "[":
                stack.append((cur_string,cur_num))
                cur_string = ""
                cur_num = 0
            elif ch == "]":
                prev_string,repeat_count = stack.pop()
                cur_string = prev_string + repeat_count * cur_string        
            else:
                cur_string+=ch
        return cur_string
