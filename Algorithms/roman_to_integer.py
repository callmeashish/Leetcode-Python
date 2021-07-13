class Solution:

    def romanToInt(self, s: str) -> int:

        roman_number_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        result = roman_number_map[s[0]]

        for index in range(1, len(s)):
            if roman_number_map[s[index-1]] >= roman_number_map[s[index]]:
                result += roman_number_map[s[index]]
            else:
                result += roman_number_map[s[index]] - 2*roman_number_map[s[index-1]]

        return result

if __name__ == "__main__":
    roman_to_int = Solution()
    print(roman_to_int.romanToInt("MCMXCIV"))          