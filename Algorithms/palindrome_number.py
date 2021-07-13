class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)

solutionObj = Solution()
print(solutionObj.isPalindrome(0))