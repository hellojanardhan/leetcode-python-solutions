# LeetCode 27 - Remove Element
# Difficulty: Easy


# Approach 1: Your Idea - Search and Swap
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def remove_element_search_swap(nums, val):
    k = 0

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] == val and nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                break

    for num in nums:
        if num != val:
            k += 1

    return k


# Approach 2: Two Pointers - Overwrite
# Recommended Interview Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def remove_element_overwrite(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k


# Approach 3: Two Pointers - Swap
# Time Complexity: O(n)
# Space Complexity: O(1)
def remove_element_swap(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k], nums[i] = nums[i], nums[k]
            k += 1

    return k


# Approach 4: Swap With Last Element
# Useful when val appears only a few times
# Time Complexity: O(n)
# Space Complexity: O(1)
def remove_element_from_end(nums, val):
    i = 0
    n = len(nums)

    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1
        else:
            i += 1

    return n


# Approach 5: Python Slice Assignment
# Python-specific approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def remove_element_pythonic(nums, val):
    nums[:] = [num for num in nums if num != val]

    return len(nums)
