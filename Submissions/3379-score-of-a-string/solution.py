class Solution:
    def scoreOfString(self, s: str) -> int:
        i,j = 0,1
        sum = 0
        while j < len(s):
            sum += abs(ord(s[j])-ord(s[i]))
            i+=1
            j+=1
        return sum
