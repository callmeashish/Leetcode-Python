"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""


class ClimbStairs:

    # Time consuming
    # Recursive way
    def climb(self, n):
        if n <= 1:
            return n
        return self.climb(n-1) + self.climb(n-2)

    def climbStairs1(self, n: int) -> int:
        return self.climb(n+1)

    # Dynamic Programming 1
    def climbStairs2(self, n: int) -> int:
        steps = {1: 1, 2: 2}

        for i in range(3, n+1):
            steps[i] = steps[i-1] + steps[i-2]

        return steps[n]

    # Dynamic Programming 2
    def climbStairs3(self, n: int) -> int:

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a = 1
            b = 2
            c = 0
            for i in range(3, n+1):
                c = a+b
                a = b
                b = c
            return c


if __name__ == '__main__':
    print(ClimbStairs().climbStairs1(3))
    print(ClimbStairs().climbStairs2(3))
    print(ClimbStairs().climbStairs3(3))
