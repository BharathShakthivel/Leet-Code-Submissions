class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        # def Positive(pali):
        #     if pali ==  pali[::-1]:
        #         return True
        #     return False  
        # rev = s[::-1]
        # if rev == s:
        #     return True
        # for i in rev:
        #     if Positive(rev.replace(i,"",1)):
        #         return True
        # return False

 
        # rev = s[::-1]
        # if rev == s:
        #     return True
        # for i in s:
        #     if (s.replace(i,"",1)) == (s.replace(i,"",1))[::-1] :
        #         return True
        # return False

        # rev = s[::-1]
        # if rev == s:
        #     return True
        
        # for i in range(len(s)):
        #     s1 = s[:i:] + s[i+1::]
        #     if s1 == s1[::-1] :
        #         return True
        # return False

        l , r = 0 , len(s)-1
        while l < r:
            if s[l]!=s[r]:
                skip_left , skip_right = s[l+1:r+1], s[l:r]
                return (skip_left == skip_left[::-1] or skip_right == skip_right[::-1])
            l+=1
            r-=1
        return True
