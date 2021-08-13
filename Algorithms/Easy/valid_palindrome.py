"""
125. Valid Palindrome

Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


class Pal:
    # Algorithmic way
    def isPalindrome1(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True

    # Pythonic way
    def isPalindrome2(self, s: str) -> bool:
        output = "".join([char for char in s.lower() if char.isalnum()])
        return output == output[::-1]


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(Pal().isPalindrome1(s))
    print(Pal().isPalindrome2(s))
