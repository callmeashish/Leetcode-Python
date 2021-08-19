"""
459. Repeated Substring Pattern

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""

from typing import List


def kmp_algo(s: str, M: int, lps: List[int]) -> List[int]:
    length = 0
    i = 1
    lps[0] = 0

    while i < M:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


class RepeatedSubstringPattern:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        lps = [0] * n
        kmp_algo(s, n, lps)
        length = lps[n - 1]

        if len(lps) > 0 and n % (n - length) == 0:
            return True
        else:
            return False
