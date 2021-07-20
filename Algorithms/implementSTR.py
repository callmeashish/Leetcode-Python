class ImplemententSTR:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        haystack_length = len(haystack)
        if needle_length == 0:
            return 0
        for i in range(0, haystack_length - needle_length + 1):
            if haystack[i : i + needle_length] == needle:
                return i

        return -1


if __name__ == "__main__":
    print(ImplemententSTR().strStr("mississippi", "sipp"))
