class LongestPalindrome:
    def longestPalindrome(self, s: str) -> str:
        if s == None or len(s) < 1:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            l1 = self.expandFromCenter(s, i, i)
            l2 = self.expandFromCenter(s, i, i + 1)
            length = max(l1, l2)
            if length > end - start:
                start = i - int((length - 1) / 2)
                end = i + int(length / 2)

        return s[start : end + 1]

    def expandFromCenter(self, s: str, left: int, right: int):
        L = left
        R = right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1

        return R - L - 1


if __name__ == "__main__":
    print(LongestPalindrome().longestPalindrome("abbcccbbbcaaccbababcbcabca"))
