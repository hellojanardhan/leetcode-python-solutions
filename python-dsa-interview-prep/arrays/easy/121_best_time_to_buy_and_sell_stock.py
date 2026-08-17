# LeetCode 121 - Best Time to Buy and Sell Stock
# Difficulty: Easy


# Approach 1: One Pass - Minimum Price
# Your Approach - Recommended / Optimal
# Time Complexity: O(n)
# Space Complexity: O(1)
def max_profit_one_pass(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


# Approach 2: One Pass Using min() and max()
# Time Complexity: O(n)
# Space Complexity: O(1)
def max_profit_min_max(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


# Approach 3: Brute Force
# Try Every Buy/Sell Combination
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def max_profit_bruteforce(prices):
    max_profit = 0

    for buy in range(len(prices)):
        for sell in range(buy + 1, len(prices)):
            profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, profit)

    return max_profit


# Approach 4: Track Maximum Future Selling Price
# Time Complexity: O(n)
# Space Complexity: O(n)
def max_profit_suffix(prices):
    n = len(prices)

    max_future = [0] * n
    max_future[-1] = prices[-1]

    for i in range(n - 2, -1, -1):
        max_future[i] = max(prices[i], max_future[i + 1])

    max_profit = 0

    for i in range(n):
        max_profit = max(
            max_profit,
            max_future[i] - prices[i]
        )

    return max_profit
