class Solution:
    def romanToInt(self, s: str) -> int:
        out = 0
        temp_dict = {"I" : 1,"V" : 5,"X" : 10,"L" : 50,"C" : 100,"D" : 500, "M" : 1000}
        for i in range(len(s)-1):
            if temp_dict[s[i]] < temp_dict[s[i+1]]:
                out-= temp_dict[s[i]]
            else:
                out += temp_dict[s[i]]          
        return out + temp_dict[s[-1]]
        
