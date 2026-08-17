# LeetCode 896 - Monotonic Array
# Difficulty: Easy


# Approach 1: Increasing and Decreasing Flags
# Your Approach - Recommended / Optimal
# Time Complexity: O(n)
# Space Complexity: O(1)
def is_monotonic_flags(nums):
    increasing = True
    decreasing = True

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            increasing = False

        if nums[i] < nums[i + 1]:
            decreasing = False

    return increasing or decreasing


# Approach 2: all()
# Pythonic Approach
# Time Complexity: O(n)
# Space Complexity: O(1) auxiliary
def is_monotonic_all(nums):
    increasing = all(
        nums[i] <= nums[i + 1]
        for i in range(len(nums) - 1)
    )

    decreasing = all(
        nums[i] >= nums[i + 1]
        for i in range(len(nums) - 1)
    )

    return increasing or decreasing


# Approach 3: Determine Direction First
# Time Complexity: O(n)
# Space Complexity: O(1)
def is_monotonic_direction(nums):
    direction = 0

    for i in range(len(nums) - 1):
        difference = nums[i + 1] - nums[i]

        if difference == 0:
            continue

        if direction == 0:
            direction = 1 if difference > 0 else -1

        elif direction * difference < 0:
            return False

    return True


# Approach 4: Compare With Sorted Arrays
# Simple Python Approach, Not Preferred for Interviews
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def is_monotonic_sorted(nums):
    return nums == sorted(nums) or nums == sorted(nums, reverse=True)
