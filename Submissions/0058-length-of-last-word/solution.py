class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # length = 0
        # x = s.strip()

        # if len(x)==1:
        #     return 1
        # for i in range((len(x)-1),-1,-1):
        #     if x[i]== " ":
        #         return length
        #     length+=1
        # return length

        i,length = len(s)-1,0
        while s[i] == " ":
            i-=1
        while i >=0 and s[i] != " ":
            length+=1
            i-=1
        return length
