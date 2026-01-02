class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = 0
        if x < 0:
            return False
        else:
         y = x       
         while y!= 0:
            digit = y % 10
            result = result * 10 + digit
            y = y // 10
         if result == x:
            return True
         else:
            return False   

           

