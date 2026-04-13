class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dict_1 = {}
        # dict_2 = {}
        # for i in s:
        #     if i in dict_1:
        #         dict_1[i] +=1
        #     else:
        #         dict_1[i] = 1
        # for j in t:
        #     if j in dict_2:
        #         dict_2[j] +=1
        #     else:
        #         dict_2[j] = 1
        # if dict_1 == dict_2:
        #     return True
        # else:
        #     return False        
        
        # New Optimal Approach: Time - (O(n)) ; Space - O(1)
        if len(s) != len(t):
            return False
        my_dict = {}
        for i in range(len(s)):
            my_dict[s[i]] = 1 + my_dict.get(s[i],0)
            my_dict[t[i]] = my_dict.get(t[i],0) - 1
        for j in my_dict.values():
            if j > 0 :
                return False
        return True
