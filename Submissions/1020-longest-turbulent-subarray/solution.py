class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        l,r  = 0,1
        n = len(arr)
        cur_sign = ""
        while (r < n):
                if cur_sign != ">" and arr[r-1] > arr[r]:
                        res = max(res,(r-l+1))
                        cur_sign = ">"
                        r+=1
                elif cur_sign != "<" and arr[r-1] < arr[r]:
                        res = max(res,(r-l+1))
                        cur_sign = "<"
                        r+=1
                else:
                    if arr[r]==arr[r-1]:
                        r = r+1
                    l = r-1
                    cur_sign = ""
        return res


