class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        """
        ptr_1 = 0
        ptr_2 = len(s)-1
        while ptr_1 < ptr_2:
            s[ptr_1],s[ptr_2] = s[ptr_2],s[ptr_1]
            ptr_1+=1
            ptr_2-=1
        
