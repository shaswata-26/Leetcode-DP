class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # Initialize a list to store the number of ways to climb to each step
        ways = [0] * (n + 1)
        ways[1] = 1  # There's only one way to reach the first step
        ways[2] = 2  # There are two ways to reach the second step
        
        # Calculate the number of ways to reach each step up to 'n'
        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]
        
        return ways[n]