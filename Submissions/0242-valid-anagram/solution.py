class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution with more space
        if len(s)!= len(t):
            return False
        my_dict_s = {}
        my_dict_t = {}

        for i in range(len(s)):
            my_dict_s[s[i]] = 1 + my_dict_s.get(s[i],0)
        for j in range(len(s)):
            my_dict_t[t[j]] = 1 + my_dict_t.get(t[j],0)
        
        if my_dict_s == my_dict_t:
            return True
        else:
            return False 
        
        # New Optimal Approach: Time - (O(n)) ; Space - O(1)
        # if len(s) != len(t):
        #     return False
        # my_dict = {}
        # for i in range(len(s)):
        #     my_dict[s[i]] = 1 + my_dict.get(s[i],0)
        #     my_dict[t[i]] = my_dict.get(t[i],0) - 1
        # for j in my_dict.values():
        #     if j > 0 :
        #         return False
        # return True
