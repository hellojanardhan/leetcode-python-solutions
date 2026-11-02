# ============================================================
# LeetCode 496 - Next Greater Element I
# Difficulty: Easy
# Topic: Arrays + Stack + HashMap
# Pattern: Monotonic Decreasing Stack
# ============================================================

# PROBLEM
# For every element in nums1, find the first greater element
# appearing to its right in nums2.
# If no greater element exists, return -1.


# ============================================================
# RECOMMENDED OPTIMAL APPROACH
# Monotonic Stack + Dictionary
# ============================================================

# Telugu + English:
# nums2 ni right nundi left ki traverse chestham.
# Stack lo next greater candidate elements ni maintain chestham.
#
# Current element kanna smaller elements stack top lo unte,
# avi next greater element avvalevu kabatti pop chestham.
#
# Stack empty kakapothe stack top is the next greater element.
# Dictionary lo result store chestham.


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        result = {}
        stack = []

        for num in reversed(nums2):

            while stack and stack[-1] < num:
                stack.pop()

            if stack:
                result[num] = stack[-1]
            else:
                result[num] = -1

            stack.append(num)

        return [result[num] for num in nums1]


# Time Complexity: O(n + m)
# n = len(nums1), m = len(nums2)
#
# Every element is pushed once and popped at most once.
# Dictionary lookup for nums1 takes O(n).
#
# Space Complexity: O(m)
# Stack + dictionary require O(m) space.


# ============================================================
# RECOMMENDED CURRENT-LEVEL APPROACH
# Brute Force Precomputation
# ============================================================

# Telugu + English:
# nums2 lo prati element ki next greater element find chestham.
# Nested loop use chesi first greater element ni identify chestham.
# Dictionary lo store chesi nums1 answers generate chestham.


class SolutionBruteForce:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        result = {}
        length = len(nums2)

        for i in range(length):
            current = nums2[i]

            for j in range(i + 1, length):

                if nums2[j] > current:
                    result[current] = nums2[j]
                    break

            else:
                result[current] = -1

        return [result[num] for num in nums1]


# Time Complexity: O(m² + n)
# Nested loops take O(m²).
# Final dictionary lookups take O(n).
#
# Space Complexity: O(m)
# Dictionary stores next greater elements for nums2.


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================

# SOLUTION 1: Direct Brute Force
# ------------------------------------------------------------
# For each nums1 element:
# 1. Find its index in nums2.
# 2. Search elements to its right.
# 3. Return the first greater element.
#
# Time: O(n * m)
# Space: O(n) for output


class Solution1:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        result = []

        for num in nums1:
            index = nums2.index(num)
            next_greater = -1

            for j in range(index + 1, len(nums2)):
                if nums2[j] > num:
                    next_greater = nums2[j]
                    break

            result.append(next_greater)

        return result


# SOLUTION 2: Brute Force Precomputation
# ------------------------------------------------------------
# Calculate next greater elements for all nums2 elements.
# Store them in a dictionary.
# Generate the final result using nums1.
#
# Time: O(m² + n)
# Space: O(m)


# SOLUTION 3: Monotonic Stack + Dictionary
# ------------------------------------------------------------
# Traverse nums2 from right to left.
# Remove smaller elements from stack.
# Stack top gives next greater element.
# Store answers in dictionary.
#
# Time: O(n + m)
# Space: O(m)
#
# BEST INTERVIEW APPROACH: SOLUTION 3


# ============================================================
# DETAILED DRY RUN
# ============================================================

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

# Traverse nums2 in reverse:
# 2 -> 4 -> 3 -> 1

# Step 1:
# Current = 2
# Stack = []
# No greater element.
# result[2] = -1
# Stack = [2]

# Step 2:
# Current = 4
# Stack = [2]
# 2 < 4, so pop 2.
# Stack becomes empty.
# result[4] = -1
# Stack = [4]

# Step 3:
# Current = 3
# Stack = [4]
# 4 > 3, so next greater element is 4.
# result[3] = 4
# Stack = [4, 3]

# Step 4:
# Current = 1
# Stack = [4, 3]
# 3 > 1, so next greater element is 3.
# result[1] = 3
# Stack = [4, 3, 1]

# Final dictionary:
# {2: -1, 4: -1, 3: 4, 1: 3}

# Final output:
# [-1, 3, -1]


# ============================================================
# TEST CASES
# ============================================================

# Test Case 1:
# nums1 = [4, 1, 2]
# nums2 = [1, 3, 4, 2]
# Output = [-1, 3, -1]

# Test Case 2:
# nums1 = [2, 4]
# nums2 = [1, 2, 3, 4]
# Output = [3, -1]

# Test Case 3:
# nums1 = [1, 3, 5]
# nums2 = [5, 4, 3, 2, 1]
# Output = [-1, -1, -1]

# Test Case 4:
# nums1 = [1]
# nums2 = [1, 2]
# Output = [2]


# ============================================================
# INTERVIEW-READY EXPLANATION
# ============================================================

# "I initially solved this problem using brute force.
# Then I optimized it using a monotonic stack and dictionary.
#
# I traverse nums2 from right to left and maintain a stack
# of potential next greater elements.
#
# Whenever the stack top is smaller than the current element,
# I pop it because it cannot be the next greater element.
#
# If the stack is not empty, its top is the next greater element.
# Otherwise, I store -1.
#
# I maintain these results in a dictionary and use it to
# construct the final answer for nums1.
#
# The optimized solution takes O(n + m) time and O(m) space."


# ============================================================
# FINAL RECOMMENDATION
# ============================================================

# Current-level approach:
# Brute Force Precomputation

# Recommended Optimal Approach:
# Monotonic Stack + Dictionary

# Important concepts:
# 1. Stack
# 2. HashMap / Dictionary
# 3. Reverse Traversal
# 4. Monotonic Decreasing Stack
# 5. Next Greater Element Pattern

# Filename:
# leetcode_496_next_greater_element_i.py

# ============================================================
# STATUS: COMPLETED
# ============================================================
