"""
383. Ransom Note

Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""


class CanConstruct:
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_list = list(ransomNote)
        magazine_list = list(magazine)
        for x in ransomNote_list:
            if x in magazine_list:
                magazine_list.remove(x)
            else:
                return False
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        for c in set(ransomNote):
            if ransomNote.count(c) > magazine.count(c):
                return False
        return True


if __name__ == '__main__':
    ransomNote = "aa"
    magazine = "aab"
    print(CanConstruct().canConstruct1(ransomNote, magazine))
    print(CanConstruct().canConstruct2(ransomNote, magazine))
