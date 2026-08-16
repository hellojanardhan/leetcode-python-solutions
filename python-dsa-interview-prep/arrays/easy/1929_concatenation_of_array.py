# LeetCode 1929 - Concatenation of Array
# Difficulty: Easy


# Approach 1: Copy + Append
# Time Complexity: O(n)
# Space Complexity: O(n)
def get_concatenation_append(nums):
    result = [*nums]
    for num in nums:
        result.append(num)
    return result

# Approach 2: List Concatenation
# Time Complexity: O(n)
# Space Complexity: O(n)
def get_concatenation_plus(nums):
    return nums + nums

# Approach 3: List Repetition
# Time Complexity: O(n)
# Space Complexity: O(n)
def get_concatenation_multiply(nums):
    return nums * 2

# Approach 4: Copy + Extend
# Time Complexity: O(n)
# Space Complexity: O(n)
def get_concatenation_extend(nums):
    result = nums.copy()
    result.extend(nums)
    return result
  
# Approach 5: Two Loops
# Time Complexity: O(n)
# Space Complexity: O(n)
def get_concatenation_two_loops(nums):
    result = []
    for num in nums:
        result.append(num)
    for num in nums:
        result.append(num)
    return result

# Approach 6: Index Based / Preallocated Array
# Time Complexity: O(n)
# Space Complexity: O(n)
def get_concatenation_index(nums):
    n = len(nums)
    result = [0] * (2 * n)
    for i in range(n):
        result[i] = nums[i]
        result[i + n] = nums[i]
    return result
  
# Approach 7: Modify Original List Using Extend
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
# Note: The original input list is modified.
def get_concatenation_inplace(nums):
    nums.extend(nums)
    return nums