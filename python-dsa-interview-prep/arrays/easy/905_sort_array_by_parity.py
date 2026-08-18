# LeetCode 905 - Sort Array By Parity
# Difficulty: Easy


# Approach 1: Separate Even and Odd Lists
# Your Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def sort_array_by_parity_lists(nums):
    even = []
    odd = []

    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return even + odd


# Approach 2: List Comprehension
# Time Complexity: O(n)
# Space Complexity: O(n)
def sort_array_by_parity_comprehension(nums):
    even = [num for num in nums if num % 2 == 0]
    odd = [num for num in nums if num % 2 != 0]

    return even + odd


# Approach 3: Two Pointers + Swap
# Recommended In-place Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def sort_array_by_parity_two_pointers(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] % 2 == 0:
            left += 1

        elif nums[right] % 2 != 0:
            right -= 1

        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums


# Approach 4: Read / Write Pointer
# Time Complexity: O(n)
# Space Complexity: O(1)
def sort_array_by_parity_write_pointer(nums):
    k = 0

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[k], nums[i] = nums[i], nums[k]
            k += 1

    return nums


# Approach 5: sorted() with Custom Key
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def sort_array_by_parity_sorted(nums):
    return sorted(nums, key=lambda num: num % 2)
