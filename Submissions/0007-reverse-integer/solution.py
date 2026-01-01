class Solution:
    def reverse(self, x: int) -> int:
        max_int = (2 ** 31)-1
        min_int = -(2 ** 31)
        output = 0
        if x >=0:
            sign = 1
        else:
            sign = -1
        x = abs(x)
        while x>0:
            last_digit = x % 10
            x = x // 10
            output = output * 10 + last_digit
            if output > max_int or output < min_int:
                return 0
        return sign * output
