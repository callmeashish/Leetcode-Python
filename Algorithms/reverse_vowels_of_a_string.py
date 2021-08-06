"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""


class ReverseVowels:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        n = len(s)
        s = list(s)
        i = 0
        j = n-1
        while i < j:
            if s[i] not in vowels:
                i += 1
            if s[j] not in vowels:
                j -= 1
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)


if __name__ == '__main__':
    print(ReverseVowels().reverseVowels("hello"))
