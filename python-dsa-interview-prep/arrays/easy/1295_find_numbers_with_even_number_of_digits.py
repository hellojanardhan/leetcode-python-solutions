# LeetCode 1295 - Find Numbers with Even Number of Digits
# Difficulty: Easy


# Approach 1: String Conversion
# Your Approach - Simple / Recommended
# Time Complexity: O(n * d)
# Space Complexity: O(d)
# d = number of digits in each number
def find_numbers_string(nums):
    count = 0

    for num in nums:
        if len(str(num)) % 2 == 0:
            count += 1

    return count


# Approach 2: Mathematical Digit Counting
# Time Complexity: O(n * d)
# Space Complexity: O(1)
def find_numbers_math(nums):
    count = 0

    for num in nums:
        digits = 0

        while num > 0:
            num //= 10
            digits += 1

        if digits % 2 == 0:
            count += 1

    return count


# Approach 3: Using log10()
# Time Complexity: O(n)
# Space Complexity: O(1)
import math


def find_numbers_log(nums):
    count = 0

    for num in nums:
        digits = int(math.log10(num)) + 1

        if digits % 2 == 0:
            count += 1

    return count


# Approach 4: Generator Expression + sum()
# Pythonic Approach
# Time Complexity: O(n * d)
# Space Complexity: O(d)
def find_numbers_generator(nums):
    return sum(
        1
        for num in nums
        if len(str(num)) % 2 == 0
    )


# Approach 5: Range Checking
# Works because of this problem's limited constraints
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_numbers_ranges(nums):
    count = 0

    for num in nums:
        if 10 <= num <= 99 or 1000 <= num <= 9999 or num == 100000:
            count += 1

    return count
