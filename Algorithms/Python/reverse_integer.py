class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        if x > 0:
            reverse = int(str(x)[::-1])
        else:
            reverse = -int(str(abs(x))[::-1])

        if(reverse < -2147483648 or reverse > 2147483647):
            return 0
        else:
            return int(reverse)