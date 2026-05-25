class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollar = 0
        ten_dollar = 0

        for bill in bills:
            if bill == 5:
                five_dollar+=1
            if bill == 10:
                ten_dollar+=1
                if five_dollar >= 1:
                    five_dollar-=1
                else:
                    return False
            if bill == 20:
                if five_dollar >= 1 and ten_dollar >=1:
                    five_dollar-=1
                    ten_dollar-=1
                elif five_dollar >=3:
                    five_dollar-=3
                else:
                    return False
        return True

