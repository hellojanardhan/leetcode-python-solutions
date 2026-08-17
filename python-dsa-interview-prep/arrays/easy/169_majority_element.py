# LeetCode 169 - Majority Element
# Difficulty: Easy


# Approach 1: Set + count()
# Your Approach
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def majority_element_count(nums):
    threshold = len(nums) // 2
    unique = set(nums)

    for num in unique:
        if nums.count(num) > threshold:
            return num


# Approach 2: Dictionary / Frequency Count
# Time Complexity: O(n)
# Space Complexity: O(n)
def majority_element_dictionary(nums):
    frequency = {}
    threshold = len(nums) // 2

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

        if frequency[num] > threshold:
            return num


# Approach 3: Counter
# Pythonic Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
from collections import Counter


def majority_element_counter(nums):
    counts = Counter(nums)

    return counts.most_common(1)[0][0]


# Approach 4: Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(n) worst case in Python sorting
def majority_element_sort(nums):
    nums.sort()

    return nums[len(nums) // 2]


# Approach 5: Boyer-Moore Voting Algorithm
# Recommended / Optimal Interview Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def majority_element_boyer_moore(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate
