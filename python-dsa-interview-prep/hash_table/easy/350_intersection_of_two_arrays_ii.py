# LeetCode 350 - Intersection of Two Arrays II
# Difficulty: Easy
# Recommended Approach: Frequency HashMap + Consume
# Recommended Current-Level Approach: Frequency HashMap + Consume


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Frequency HashMap + Consume
# Your Approach
# Recommended HashMap Approach
# Time Complexity: O(n + m)
# Space Complexity: O(n)
#
# Time Explanation:
# nums1 ni traverse chesi frequencies build cheyadaniki O(n).
# nums2 ni traverse chesi matching numbers find cheyadaniki O(m).
# Dictionary operations average-ga O(1).
# Kabatti total time complexity O(n + m).
#
# Space Explanation:
# nums1 lo unique numbers frequencies dictionary lo store chestunnam.
# Worst case lo nums1 lo n unique numbers undavachu.
# Kabatti auxiliary space complexity O(n).
class Solution1:
    def intersect(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> List[int]:
        frequency = {}
        result = []

        for number in nums1:
            frequency[number] = frequency.get(number, 0) + 1

        for number in nums2:
            if frequency.get(number, 0) > 0:
                result.append(number)
                frequency[number] -= 1

        return result


# ============================================================


# Approach 2: Frequency HashMap of Smaller Array
# Recommended Space-Optimized HashMap Approach
# Time Complexity: O(n + m)
# Space Complexity: O(min(n, m))
#
# Time Explanation:
# Rendu arrays ni total-ga okkokkasari process chestunnam.
# Kabatti total time complexity O(n + m).
#
# Space Explanation:
# Chinna array frequencies maatrame dictionary lo store chestunnam.
# Kabatti auxiliary space complexity O(min(n, m)).
class Solution2:
    def intersect(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        frequency = {}

        for number in nums1:
            frequency[number] = frequency.get(number, 0) + 1

        result = []

        for number in nums2:
            if frequency.get(number, 0) > 0:
                result.append(number)
                frequency[number] -= 1

        return result


# ============================================================


# Approach 3: Sorting + Two Pointers
# Recommended Without HashMap
# Time Complexity: O(n log n + m log m)
# Space Complexity: O(n + m) with sorted()
#
# Time Explanation:
# nums1 ni sort cheyadaniki O(n log n).
# nums2 ni sort cheyadaniki O(m log m).
# Two pointers traversal O(n + m).
#
# Space Explanation:
# sorted() rendu new lists create chestundi.
# Kabatti auxiliary space complexity O(n + m).
#
# If input arrays ni direct-ga .sort() chesthe,
# Python sort internal memory ni ignore chesinaప్పుడు O(1) auxiliary
# ani sometimes simplify chestaru. Kaani inputs modify avutayi.
class Solution3:
    def intersect(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> List[int]:
        first = sorted(nums1)
        second = sorted(nums2)

        left = 0
        right = 0
        result = []

        while left < len(first) and right < len(second):
            if first[left] == second[right]:
                result.append(first[left])
                left += 1
                right += 1

            elif first[left] < second[right]:
                left += 1

            else:
                right += 1

        return result


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Counter Intersection
# Short Python Approach
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
#
# Time Explanation:
# Counter rendu arrays frequencies calculate chestundi.
# Counter intersection minimum common frequencies teesukuntundi.
# elements() result numbers ni required count prakaram generate chestundi.
#
# Space Explanation:
# Rendu arrays frequencies Counters lo store avutayi.
class Solution4:
    def intersect(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> List[int]:
        from collections import Counter

        common = Counter(nums1) & Counter(nums2)

        return list(common.elements())


# ============================================================


# Approach 5: List Membership + remove()
# Brute Force Approach
# Time Complexity: O(n * m)
# Space Complexity: O(n)
#
# Time Explanation:
# Prati nums2 number kosam copy list lo membership check chestunnam.
# List membership mariyu remove operations O(n).
# Kabatti worst-case time complexity O(n * m).
#
# Space Explanation:
# nums1 copy create chestunnam.
# Kabatti auxiliary space complexity O(n).
class Solution5:
    def intersect(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> List[int]:
        available = nums1.copy()
        result = []

        for number in nums2:
            if number in available:
                result.append(number)
                available.remove(number)

        return result
