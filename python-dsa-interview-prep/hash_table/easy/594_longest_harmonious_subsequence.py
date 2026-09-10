# LeetCode 594 - Longest Harmonious Subsequence
# Difficulty: Easy

# Recommended Approach: Frequency HashMap
# Recommended Current-Level Approach: Frequency HashMap


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Frequency HashMap
# Your Approach
# Recommended Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# Array lo prati number ni okasari traverse chesi frequency calculate chestunnam.
# Tarvata k unique values ni traverse chestunnam.
# Prati value kosam value + 1 HashMap lo undho check chestunnam.
# Dictionary lookup average-ga O(1).
# Kabatti total time O(n + k), simplified-ga O(n).
#
# Space Explanation:
# k unique numbers frequencies ni dictionary lo store chestunnam.
# Kabatti auxiliary space complexity O(k).
class Solution1:
    def findLHS(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        count = 0

        for value in freq:
            if value + 1 in freq:
                length = freq[value] + freq[value + 1]
                count = max(count, length)

        return count


# ============================================================


# Approach 2: Counter + Adjacent Frequency Lookup
# Short Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# Counter array elements frequencies ni O(n) time lo calculate chestundi.
# Tarvata k unique values ni traverse chesi value + 1 frequency undho check chestunnam.
# Counter lookup average-ga O(1).
# Kabatti total time complexity O(n + k), simplified-ga O(n).
#
# Space Explanation:
# Counter lo maximum k unique numbers store avutayi.
# Kabatti auxiliary space complexity O(k).
class Solution2:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter

        frequency = Counter(nums)
        result = 0

        for value in frequency:
            if value + 1 in frequency:
                result = max(
                    result,
                    frequency[value] + frequency[value + 1]
                )

        return result


# ============================================================


# Approach 3: Sorting + Sliding Window
# Recommended Alternative Approach
# Time Complexity: O(n log n)
# Space Complexity: O(n) worst-case in Python sorting
#
# Time Explanation:
# Munduga array ni sort chestunnam, kabatti O(n log n).
# Tarvata left and right pointers tho array ni sliding window laga traverse chestunnam.
# nums[right] - nums[left] > 1 ayite left pointer ni move chestunnam.
# Difference exactly 1 ayite current window harmonious subsequence candidate.
# Sliding window traversal O(n).
# Kabatti total time complexity O(n log n + n), simplified-ga O(n log n).
#
# Space Explanation:
# nums.sort() list ni in-place modify chestundi.
# Kaani Python Timsort implementation worst-case lo extra memory use cheyyachu.
# Kabatti worst-case auxiliary space O(n).
class Solution3:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()

        left = 0
        result = 0

        for right in range(len(nums)):

            while nums[right] - nums[left] > 1:
                left += 1

            if nums[right] - nums[left] == 1:
                result = max(
                    result,
                    right - left + 1
                )

        return result


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Sorting + Group Frequency Counting
# Time Complexity: O(n log n)
# Space Complexity: O(n) worst-case in Python sorting
#
# Time Explanation:
# Array ni sort cheyadaniki O(n log n).
# Sorted array lo same values consecutive-ga untayi.
# Prati value group frequency ni calculate chestunnam.
# Previous distinct value current value ki difference 1 ayite
# rendu group frequencies ni add chesi maximum calculate chestunnam.
# Group traversal O(n).
# Kabatti total time complexity O(n log n).
#
# Space Explanation:
# Extra HashMap use cheyyatledu.
# Kaani Python sorting worst-case lo temporary memory use cheyyachu.
# Kabatti worst-case auxiliary space O(n).
class Solution4:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()

        result = 0
        previous_value = None
        previous_count = 0

        index = 0

        while index < len(nums):
            current_value = nums[index]
            current_count = 0

            while (
                index < len(nums)
                and nums[index] == current_value
            ):
                current_count += 1
                index += 1

            if (
                previous_value is not None
                and current_value - previous_value == 1
            ):
                result = max(
                    result,
                    previous_count + current_count
                )

            previous_value = current_value
            previous_count = current_count

        return result


# ============================================================


# Approach 5: Brute Force Using count()
# Time Complexity: O(n^2)
# Space Complexity: O(k)
#
# Time Explanation:
# Munduga unique numbers kosam set create chestunnam.
# Prati unique value kosam nums.count(value)
# mariyu nums.count(value + 1) complete array ni scan chestayi.
# arr.count() O(n).
# Worst-case lo k nearly n unique values undavachu.
# Kabatti total worst-case time complexity O(n^2).
#
# Space Explanation:
# Unique values ni set lo store chestunnam.
# Maximum k unique elements untayi.
# Kabatti auxiliary space complexity O(k).
class Solution5:
    def findLHS(self, nums: List[int]) -> int:
        unique_values = set(nums)
        result = 0

        for value in unique_values:

            if value + 1 in unique_values:
                current_count = nums.count(value)
                next_count = nums.count(value + 1)

                result = max(
                    result,
                    current_count + next_count
                )

        return result
