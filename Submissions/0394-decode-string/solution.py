class Solution:
    def decodeString(self, s: str) -> str:
        '''
        # 1. Initialize:
        #       - stack = []
        #       - current_string = ""
        #       - current_number = 0
        #
        # 2. Traverse each character in the string:
        #
        #    If digit:
        #        Build the full number (current_number = current_number * 10 + digit)
        #
        #    If "[":
        #        Push (current_string, current_number) to stack
        #        Reset current_string = ""
        #        Reset current_number = 0
        #
        #    If "]":
        #        Pop last (prev_string, repeat_count) from stack
        #        current_string = prev_string + repeat_count * current_string
        #
        #    Else (letter):
        #        Append to current_string
        #
        # 3. Return current_string
        '''        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
