"""
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.


Example 2:

Input: s = "a"
Output: 1
Example 3:

Input: s = "bb"
Output: 2
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""


from typing import Counter


class Pal:
    def longestPalindrome(self, s: str) -> int:
        look = dict(Counter(s))

        final = 0
        added = 0

        for j in look.values():
            if j > 1:
                final += j // 2
            if j % 2 == 1:
                added = 1

        return 2 * final + added


if __name__ == "__main__":
    s = "abccccdd"
    print(Pal().longestPalindrome(s))
