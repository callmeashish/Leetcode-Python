"""
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""


class FirstUniqChar:
    def firstUniqChar(self, s: str) -> int:
        char_dict = {}
        repeating_stack = {}
        for i, c in enumerate(s):
            if c in char_dict:
                char_dict.pop(c)
                repeating_stack[c] = i
            elif c not in repeating_stack:
                char_dict[c] = i

        return min(char_dict.values()) if char_dict else -1


if __name__ == '__main__':
    print(FirstUniqChar().firstUniqChar("abab"))
