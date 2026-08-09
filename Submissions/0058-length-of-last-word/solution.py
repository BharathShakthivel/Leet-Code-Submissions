class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        x = s.strip()

        if len(x)==1:
            return 1
        for i in range((len(x)-1),-1,-1):
            if x[i]== " ":
                return length
            length+=1
        return length
