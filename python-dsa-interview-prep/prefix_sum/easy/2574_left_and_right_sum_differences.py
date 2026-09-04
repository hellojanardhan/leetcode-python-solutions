# LeetCode 2574 - Left and Right Sum Differences
# Difficulty: Easy
#
# Recommended Optimal Approach: Total Sum + Running Left Sum
# Your Approach: Prefix Left Array + Suffix Right Array


# ============================================================
# Approach 1: Left and Right Arrays
# Your Approach
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(n)
# ============================================================

class Solution1:
    def leftRightDifference(
        self,
        nums: List[int]
    ) -> List[int]:

        n = len(nums)

        left = [0] * n

        for i in range(1, n):
            left[i] = left[i - 1] + nums[i - 1]

        right = [0] * n

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] + nums[i + 1]

        result = [0] * n

        for i in range(n):
            result[i] = abs(left[i] - right[i])

        return result


# ============================================================
# Approach 2: Total Sum + Running Left Sum
# Recommended Optimal Approach
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
# ============================================================
#
# right_sum = total_sum - left_sum - current_value

class Solution2:
    def leftRightDifference(
        self,
        nums: List[int]
    ) -> List[int]:

        total_sum = sum(nums)
        left_sum = 0
        result = []

        for value in nums:
            right_sum = total_sum - left_sum - value

            result.append(
                abs(left_sum - right_sum)
            )

            left_sum += value

        return result


# ============================================================
# Approach 3: Use Result Array as Left-Sum Storage
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
# ============================================================

class Solution3:
    def leftRightDifference(
        self,
        nums: List[int]
    ) -> List[int]:

        n = len(nums)
        result = [0] * n

        left_sum = 0

        for i in range(n):
            result[i] = left_sum
            left_sum += nums[i]

        right_sum = 0

        for i in range(n - 1, -1, -1):
            result[i] = abs(result[i] - right_sum)
            right_sum += nums[i]

        return result


# ============================================================
# Approach 4: Brute Force
# Time Complexity: O(n²)
# Auxiliary Space Complexity: O(1)
# ============================================================

class Solution4:
    def leftRightDifference(
        self,
        nums: List[int]
    ) -> List[int]:

        n = len(nums)
        result = []

        for i in range(n):
            left_sum = 0
            right_sum = 0

            for j in range(i):
                left_sum += nums[j]

            for j in range(i + 1, n):
                right_sum += nums[j]

            result.append(
                abs(left_sum - right_sum)
            )

        return result
