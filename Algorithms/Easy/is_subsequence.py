"""
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""


class Subseq:
    # Single pointer approach
    def isSubsequence1(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        ni = len(s)
        nj = len(t)

        while i < ni and j < nj:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == ni

    # Double pointer approach
    def isSubsequence2(self, s: str, t: str) -> bool:
        i = 0
        j = len(s) - 1

        ii = 0
        jj = len(t) - 1

        while i <= j and ii <= jj:

            if s[i] == t[ii]:
                i += 1
            if s[j] == t[jj]:
                j -= 1

            ii += 1
            jj -= 1

        return i > j


if __name__ == "__main__":
    s = "abgc"
    t = "ahbgdc"
    print(Subseq().isSubsequence1(s, t))
    print(Subseq().isSubsequence2(s, t))
