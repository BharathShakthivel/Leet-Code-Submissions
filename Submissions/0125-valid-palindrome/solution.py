class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Solution 1

        # import re
        # result = (re.sub(r'[^a-zA-Z0-9]', '', s)).lower()
        # if result == "":
        #     return True
        # elif result == result[::-1]:
        #     return True
        # else:
        #     return False

        # Lite Polish

        # import re
        # result = (re.sub(r'[^a-zA-Z0-9]', '', s)).lower()
        # if result == "":
        #     return True
        # elif result != result[::-1]:
        #     return False
        # return True


        # More Polish
        # import re
        # result = (re.sub(r'[^a-zA-Z0-9]', '', s)).lower()
        # if result != result[::-1]:
        #     return False
        # return True

        # “I first normalize the string by removing non-alphanumeric characters and converting everything to lowercase. Then I check whether the cleaned string is equal to its reverse. If it is, it’s a palindrome.”

        # import re
        # s = (re.sub(r'[^a-zA-Z0-9]', '', s)).lower()
        # if s != s[::-1]:
        #     return False
        # return True

        # Two pointer Approach
        import re
        s = (re.sub(r'[^a-zA-Z0-9]', '', s)).lower()
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return False
        return True
