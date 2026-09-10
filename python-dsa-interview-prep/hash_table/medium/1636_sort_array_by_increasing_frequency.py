# LeetCode 1636 - Sort Array by Increasing Frequency
# Difficulty: Easy
#
# Recommended Approach:
# Frequency HashMap + Custom Sorting
#
# Recommended Current-Level Approach:
# Frequency HashMap + Custom Sorting


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Frequency HashMap + Sort Unique Values
# Your Approach — Cleaned
# Recommended Current-Level Approach
#
# Time Complexity: O(n + u log u)
# Worst Case: O(n log n)
# Space Complexity: O(n), including output
#
# u = number of unique values

class Solution1:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = {}

        for number in nums:
            frequency[number] = frequency.get(number, 0) + 1

        sorted_items = sorted(
            frequency.items(),
            key=lambda item: (
                item[1],     # Frequency increasing
                -item[0]     # Value decreasing
            )
        )

        result = []

        for value, count in sorted_items:
            result.extend([value] * count)

        return result


# ============================================================
# Approach 2: Frequency HashMap + Sort Original Array
# Short Recommended Approach
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#
# Original array elementsనే custom keyతో sort చేస్తున్నాం.

class Solution2:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = {}

        for number in nums:
            frequency[number] = frequency.get(number, 0) + 1

        return sorted(
            nums,
            key=lambda number: (
                frequency[number],
                -number
            )
        )


# ============================================================
# Approach 3: Fixed Frequency Array
# Constraint-Based Optimal-Time Approach
#
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
# Output Space: O(n)
#
# Problem constraints:
# -100 <= nums[i] <= 100
#
# Total possible values = 201, which is constant.

class Solution3:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = [0] * 201

        for number in nums:
            frequency[number + 100] += 1

        result = []

        for count in range(1, len(nums) + 1):
            for value in range(100, -101, -1):
                if frequency[value + 100] == count:
                    result.extend([value] * count)

        return result


# ============================================================
# OTHER USEFUL SOLUTIONS
# ============================================================


# Approach 4: Counter + Custom Sorting
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution4:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter

        frequency = Counter(nums)

        return sorted(
            nums,
            key=lambda number: (
                frequency[number],
                -number
            )
        )


# ============================================================
# Approach 5: count() + Sorting
# Brute-Force Python Approach
#
# Time Complexity: O(n²)
# Space Complexity: O(n)
#
# nums.count(number) ప్రతి number కోసం complete array scan చేస్తుంది.

class Solution5:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(
            nums,
            key=lambda number: (
                nums.count(number),
                -number
            )
        )
