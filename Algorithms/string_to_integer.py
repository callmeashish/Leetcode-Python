class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        start = 0
        number = 0
        s = s.strip()

        if s == "":
            return 0
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            sign = 1
            s = s[1:]

        while start < len(s) and s[start].isnumeric():
            number = number * 10 + int(s[start])
            start += 1

        number = number * sign

        if number < -2147483648:
            number = -2147483648
        elif number > 2147483647:
            number = 2147483647

        return number


if __name__ == "__main__":
    print(Solution().myAtoi("+42"))
