# LeetCode 485 - Max Consecutive Ones
# Difficulty: Easy


# Approach 1: Running Count
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_max_consecutive_ones(nums):
    maximum = 0
    count = 0

    for num in nums:
        if num == 1:
            count += 1
            maximum = max(maximum, count)
        else:
            count = 0

    return maximum


# Approach 2: Update Maximum When Zero Appears
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_max_consecutive_ones_on_zero(nums):
    maximum = 0
    count = 0

    for num in nums:
        if num == 1:
            count += 1
        else:
            maximum = max(maximum, count)
            count = 0

    return max(maximum, count)


# Approach 3: String Conversion + Split
# Time Complexity: O(n)
# Space Complexity: O(n)
def find_max_consecutive_ones_string(nums):
    text = "".join(map(str, nums))
    groups = text.split("0")

    return max(len(group) for group in groups)


# Approach 4: itertools.groupby()
# Time Complexity: O(n)
# Space Complexity: O(1) Auxiliary
from itertools import groupby


def find_max_consecutive_ones_groupby(nums):
    maximum = 0

    for value, group in groupby(nums):
        if value == 1:
            count = sum(1 for _ in group)
            maximum = max(maximum, count)

    return maximum
