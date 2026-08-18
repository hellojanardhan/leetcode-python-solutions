# LeetCode 977 - Squares of a Sorted Array
# Difficulty: Easy


# Approach 1: Square + Sort
# Your Approach
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def sorted_squares_sort(nums):
    return sorted([num ** 2 for num in nums])


# Approach 2: Two Pointers
# Recommended / Optimal
# Time Complexity: O(n)
# Space Complexity: O(n)
def sorted_squares_two_pointers(nums):
    left = 0
    right = len(nums) - 1

    result = [0] * len(nums)

    position = len(nums) - 1

    while left <= right:

        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[position] = left_square
            left += 1
        else:
            result[position] = right_square
            right -= 1

        position -= 1

    return result


# Approach 3: Two Pointers + Append + Reverse
# Time Complexity: O(n)
# Space Complexity: O(n)
def sorted_squares_reverse(nums):
    left = 0
    right = len(nums) - 1

    result = []

    while left <= right:

        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left] ** 2)
            left += 1
        else:
            result.append(nums[right] ** 2)
            right -= 1

    return result[::-1]


# Approach 4: map() + sorted()
# Pythonic Alternative
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def sorted_squares_map(nums):
    return sorted(map(lambda num: num ** 2, nums))
