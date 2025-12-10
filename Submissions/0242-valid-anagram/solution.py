class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1 = {}
        dict_2 = {}
        for i in s:
            if i in dict_1:
                dict_1[i] +=1
            else:
                dict_1[i] = 1
        for j in t:
            if j in dict_2:
                dict_2[j] +=1
            else:
                dict_2[j] = 1
        if dict_1 == dict_2:
            return True
        else:
            return False        
        
