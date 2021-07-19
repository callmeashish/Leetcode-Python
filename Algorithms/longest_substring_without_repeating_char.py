class LongestSub:
    def solution1(self, s: str) -> int:
        length = len(s)
        if (length <= 1) or (length == 2 and s[0] != s[1]):
            return length

        else:
            used_char = {}
            start = 0
            max_length = 0
            for i, c in enumerate(s):
                if c in used_char:
                    start = max(start, used_char[c] + 1)
                used_char[c] = i
                max_length = max(max_length, i - start + 1)

        return max_length

    def solution1(self, s: str) -> int:
        length = len(s)
        if (length <= 1) or (length == 2 and s[0] != s[1]):
            return length
        longest_sub1 = ""
        longest_sub2 = ""
        for char in s:
            if char not in longest_sub1:
                longest_sub1 += char
            else:
                if len(longest_sub1) > len(longest_sub2):
                    longest_sub2 = longest_sub1
                longest_sub1 = longest_sub1.split(char)[1] + char
        if len(longest_sub1) > len(longest_sub2):
            longest_sub2 = longest_sub1
        return len(longest_sub2)


if __name__ == "__main__":
    print(LongestSub().lengthOfLongestSubstring("abcabcbb"))
