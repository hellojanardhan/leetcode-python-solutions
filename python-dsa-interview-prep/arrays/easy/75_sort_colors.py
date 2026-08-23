# LeetCode 75 - Sort Colors
# Difficulty: Medium


# Approach 1: Dutch National Flag / Three Pointers
# Your Approach - Recommended / Optimal
# Time Complexity: O(n)
# Space Complexity: O(1)
def sort_colors_three_pointers(nums):
    left = 0
    current = 0
    right = len(nums) - 1

    while current <= right:
        if nums[current] == 0:
            nums[left], nums[current] = nums[current], nums[left]
            left += 1
            current += 1

        elif nums[current] == 1:
            current += 1

        else:
            nums[current], nums[right] = nums[right], nums[current]
            right -= 1


# Approach 2: Counting 0s, 1s and 2s
# Two Passes
# Time Complexity: O(n)
# Space Complexity: O(1)
def sort_colors_counting(nums):
    zeros = 0
    ones = 0
    twos = 0

    for num in nums:
        if num == 0:
            zeros += 1
        elif num == 1:
            ones += 1
        else:
            twos += 1

    index = 0

    for _ in range(zeros):
        nums[index] = 0
        index += 1

    for _ in range(ones):
        nums[index] = 1
        index += 1

    for _ in range(twos):
        nums[index] = 2
        index += 1


# Approach 3: Counting Using count()
# Simple Python Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def sort_colors_count(nums):
    zeros = nums.count(0)
    ones = nums.count(1)
    twos = nums.count(2)

    nums[:] = (
        [0] * zeros
        + [1] * ones
        + [2] * twos
    )


# Approach 4: Manual Bubble Sort
# Works, but not recommended
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def sort_colors_bubble(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


# Approach 5: Built-in sort()
# NOT ALLOWED by the problem
# Time Complexity: O(n log n)
def sort_colors_builtin(nums):
    nums.sort()
