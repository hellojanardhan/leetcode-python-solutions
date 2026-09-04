# LeetCode 2485 - Find the Pivot Integer
# Difficulty: Easy
#
# Recommended Optimal Approach: Mathematical Perfect-Square Check
# Recommended Current-Level Approach: Running Left and Right Sums


# ============================================================
# Approach 1: Slicing + sum()
# Your Approach — Cleaned
# Time Complexity: O(n²)
# Space Complexity: O(n)
# ============================================================

class Solution1:
    def pivotInteger(self, n: int) -> int:
        numbers = [
            number
            for number in range(1, n + 1)
        ]

        for index in range(n):
            left_sum = sum(numbers[:index + 1])
            right_sum = sum(numbers[index:])

            if left_sum == right_sum:
                return numbers[index]

        return -1


# ============================================================
# Approach 2: Running Left and Right Sums
# Recommended Current-Level Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
# ============================================================

class Solution2:
    def pivotInteger(self, n: int) -> int:
        left_sum = 0
        right_sum = n * (n + 1) // 2

        for number in range(1, n + 1):
            left_sum += number

            if left_sum == right_sum:
                return number

            right_sum -= number

        return -1


# ============================================================
# Approach 3: Mathematical Perfect-Square Check
# Recommended Optimal Approach
# Time Complexity: O(1)
# Space Complexity: O(1)
# ============================================================
#
# Required:
# sum(1...x) == sum(x...n)
#
# Simplification:
# x² = n * (n + 1) // 2
#
# Total sum perfect square ayithe,
# aa square root pivot integer avutundi.

class Solution3:
    def pivotInteger(self, n: int) -> int:
        from math import isqrt

        total_sum = n * (n + 1) // 2
        pivot = isqrt(total_sum)

        if pivot * pivot == total_sum:
            return pivot

        return -1


# ============================================================
# Approach 4: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)
# ============================================================

class Solution4:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2

        left = 1
        right = n

        while left <= right:
            middle = (left + right) // 2
            square = middle * middle

            if square == total_sum:
                return middle

            if square < total_sum:
                left = middle + 1
            else:
                right = middle - 1

        return -1
