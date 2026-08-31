# LeetCode 1512 - Number of Good Pairs
# Difficulty: Easy
# Recommended Approach: Frequency HashMap - Count Previous Occurrences
# Recommended Current-Level Approach: Frequency HashMap


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Frequency HashMap - Count Previous Occurrences
# Recommended Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# nums array ni okasari traverse chestunnam.
# Current number mundu enni times vachindo HashMap nundi O(1)
# average time lo lookup chestunnam.
# Aa previous occurrences anni current number tho good pairs form chestayi.
# Kabatti total time complexity O(n).
#
# Space Explanation:
# k unique numbers frequencies ni dictionary lo store chestunnam.
# Kabatti auxiliary space complexity O(k).
class Solution1:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        frequency = {}
        pairs = 0

        for num in nums:
            pairs += frequency.get(num, 0)
            frequency[num] = frequency.get(num, 0) + 1

        return pairs


# ============================================================


# Approach 2: Frequency HashMap + Combination Formula
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# First nums array ni traverse chesi prati number frequency calculate chestunnam.
# Tarvata k unique frequencies ni traverse chestunnam.
# Oka number c times occur ayithe,
# possible good pairs = c * (c - 1) // 2.
# Kabatti total time complexity O(n + k), simplified-ga O(n).
#
# Space Explanation:
# k unique numbers frequencies dictionary lo store chestunnam.
# Kabatti auxiliary space complexity O(k).
class Solution2:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        pairs = 0

        for count in frequency.values():
            pairs += count * (count - 1) // 2

        return pairs


# ============================================================


# Approach 3: Nested Loops
# Your Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
#
# Time Explanation:
# Prati index i kosam remaining indexes j ni compare chestunnam.
# First element roughly n-1 comparisons,
# next element n-2 comparisons, ala continue avutundi.
# Total comparisons approximately n * (n - 1) / 2.
# Kabatti time complexity O(n^2).
#
# Space Explanation:
# Extra dictionary, set, list lantivi use cheyyatledu.
# count, i, j variables matrame use chestunnam.
# Kabatti auxiliary space complexity O(1).
class Solution3:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1

        return count


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Counter + Combination Formula
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# Counter nums frequencies ni O(n) time lo calculate chestundi.
# Tarvata unique frequency values ni traverse chesi
# c * (c - 1) // 2 formula apply chestunnam.
# Kabatti total time complexity O(n).
#
# Space Explanation:
# Counter lo maximum k unique entries untayi.
# Kabatti auxiliary space complexity O(k).
class Solution4:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import Counter

        frequency = Counter(nums)

        pairs = 0

        for count in frequency.values():
            pairs += count * (count - 1) // 2

        return pairs


# ============================================================


# Approach 5: Sorting + Group Counting
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#
# Time Explanation:
# sorted() array ni sort cheyadaniki O(n log n).
# Tarvata same numbers groups ni linear-ga O(n) time lo count chestunnam.
# Prati group count c kosam c * (c - 1) // 2 pairs add chestunnam.
# Kabatti total time complexity O(n log n).
#
# Space Explanation:
# sorted() kotta sorted list create chestundi.
# Kabatti auxiliary space complexity O(n).
class Solution5:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums = sorted(nums)

        pairs = 0
        i = 0

        while i < len(nums):
            j = i

            while j < len(nums) and nums[j] == nums[i]:
                j += 1

            count = j - i
            pairs += count * (count - 1) // 2

            i = j

        return pairs
