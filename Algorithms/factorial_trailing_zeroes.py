class Solution:
    @staticmethod
    def trailingZeroes(n: int) -> int:
        count = 0
        while n > 0:
            n = n // 5
            count += n
        return count


if __name__ == "__main__":
    number = 10
    print(Solution.trailingZeroes(number))
