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
        import re
        result = (re.sub(r'[^a-zA-Z0-9]', '', s)).lower()
        if result != result[::-1]:
            return False
        return True
