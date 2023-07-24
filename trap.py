class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        left_max = [0] * n  # To store the maximum height to the left of each position
        right_max = [0] * n  # To store the maximum height to the right of each position

        # Calculate the maximum height to the left of each position
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # Calculate the maximum height to the right of each position
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        trapped_water = 0
        for i in range(n):
            # Calculate the trapped water at each position and add it to the total
            trapped_water += min(left_max[i], right_max[i]) - height[i]

        return trapped_water