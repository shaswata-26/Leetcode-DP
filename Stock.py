from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        # Initialize the DP table with 0 values
        dp = [0] * n

        # Initialize the minimum price to the first element
        min_price = prices[0]

        for i in range(1, n):
            # Update the minimum price seen so far
            min_price = min(min_price, prices[i])

            # Calculate the maximum profit at this point and update the DP table
            dp[i] = max(dp[i - 1], prices[i] - min_price)

        return dp[n - 1]

# # Example usage:
# prices = [7, 1, 5, 3, 6, 4]
# solution = Solution()
# print(solution.maxProfit(prices))  # Output: 5
