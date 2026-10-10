class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # to make maximum profit you want to find the biggest variance (low to high) that you can find
        

        # Approach 1: Brute-Force
        # For each price, calculate the difference between it and prices in the future, take the max
        # Time Complexity: O(n^2)

        # Approach 2: Sliding Window???
        # In a certain window, keep track of the max and min


        min_so_far = prices[0]
        max_difference = 0

        for i in range(len(prices)):
            if prices[i] < min_so_far:
                min_so_far = prices[i]
            elif prices[i] > min_so_far:
                max_difference = max(max_difference, prices[i] - min_so_far)

        return max_difference
