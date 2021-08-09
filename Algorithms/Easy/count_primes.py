"""
204. Count Primes

Count the number of prime numbers less than a non-negative number, n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106
"""


class CountPrimes:
    def countPrimes1(self, n: int) -> int:
        prime = [True] * (n + 1)
        p = 2

        while p * p <= n:
            if prime[p] == True:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        c = 0

        for p in range(2, n):
            if prime[p]:
                c += 1
        return c


if __name__ == "__main__":
    print(CountPrimes().countPrimes1(10))
