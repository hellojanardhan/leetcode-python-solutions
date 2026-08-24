# LeetCode 219 - Contains Duplicate II
# Difficulty: Easy


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: HashMap - Value -> Last Seen Index
# Your Approach
# Recommended / Optimal Interview Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution1:
    def containsNearbyDuplicate(self, nums, k):

        seen = {}

        for index in range(len(nums)):
            current_value = nums[index]

            if current_value in seen:
                previous_index = seen[current_value]

                if index - previous_index <= k:
                    return True

            # Store latest occurrence
            seen[current_value] = index

        return False


# ============================================================


# Approach 2: HashMap using enumerate()
# Cleaner Python version
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution2:
    def containsNearbyDuplicate(self, nums, k):

        seen = {}

        for index, value in enumerate(nums):

            if value in seen and index - seen[value] <= k:
                return True

            seen[value] = index

        return False


# ============================================================


# Approach 3: Sliding Window + Set
# Maintain only last k elements
# Time Complexity: O(n)
# Space Complexity: O(k)
class Solution3:
    def containsNearbyDuplicate(self, nums, k):

        window = set()

        for index, value in enumerate(nums):

            if value in window:
                return True

            window.add(value)

            if len(window) > k:
                window.remove(nums[index - k])

        return False


# ============================================================
# REMAINING SOLUTIONS
# ============================================================


# Approach 4: Brute Force
# Compare each value with next k positions
# Time Complexity: O(n * k)
# Space Complexity: O(1)
class Solution4:
    def containsNearbyDuplicate(self, nums, k):

        for i in range(len(nums)):

            for j in range(i + 1, min(len(nums), i + k + 1)):

                if nums[i] == nums[j]:
                    return True

        return False
