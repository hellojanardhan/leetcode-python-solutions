# LeetCode 454 - 4Sum II
# Difficulty: Medium
#
# Recommended Optimal Approach:
# Pair-Sum Frequency HashMap
#
# Recommended Current-Level Approach:
# Pair-Sum Frequency HashMap


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: One Pair-Sum Frequency HashMap
# Your Approach — Cleaned
# Recommended Optimal Approach
#
# Time Complexity: O(n²)
# Space Complexity: O(n²)
#
# First two arrays pair sums build cheyadaniki O(n²).
# Last two arrays pair sums check cheyadaniki O(n²).
# Total O(2n²), simplified-ga O(n²).

class Solution1:
    def fourSumCount(
        self,
        nums1: List[int],
        nums2: List[int],
        nums3: List[int],
        nums4: List[int]
    ) -> int:

        pair_frequency = {}

        for first in nums1:
            for second in nums2:
                pair_sum = first + second

                pair_frequency[pair_sum] = (
                    pair_frequency.get(pair_sum, 0) + 1
                )

        count = 0

        for third in nums3:
            for fourth in nums4:
                required = -(third + fourth)

                count += pair_frequency.get(required, 0)

        return count


# ============================================================
# Approach 2: Two Pair-Sum Counters
#
# Time Complexity: O(n²)
# Space Complexity: O(n²)
#
# Both halves pair-sum frequencies calculate chesi,
# opposite sums frequencies multiply chestunnam.

class Solution2:
    def fourSumCount(
        self,
        nums1: List[int],
        nums2: List[int],
        nums3: List[int],
        nums4: List[int]
    ) -> int:

        from collections import Counter

        first_half = Counter(
            first + second
            for first in nums1
            for second in nums2
        )

        second_half = Counter(
            third + fourth
            for third in nums3
            for fourth in nums4
        )

        count = 0

        for pair_sum, frequency in first_half.items():
            count += (
                frequency
                * second_half.get(-pair_sum, 0)
            )

        return count


# ============================================================
# Approach 3: Sorted Pair Sums + Two Pointers
#
# Time Complexity: O(n² log n)
# Space Complexity: O(n²)
#
# Equal pair sums group sizes multiply cheyali.
# HashMap use cheyani alternative.

class Solution3:
    def fourSumCount(
        self,
        nums1: List[int],
        nums2: List[int],
        nums3: List[int],
        nums4: List[int]
    ) -> int:

        first_sums = sorted(
            first + second
            for first in nums1
            for second in nums2
        )

        second_sums = sorted(
            third + fourth
            for third in nums3
            for fourth in nums4
        )

        left = 0
        right = len(second_sums) - 1
        count = 0

        while left < len(first_sums) and right >= 0:
            total = first_sums[left] + second_sums[right]

            if total < 0:
                left += 1

            elif total > 0:
                right -= 1

            else:
                first_value = first_sums[left]
                second_value = second_sums[right]

                first_count = 0
                second_count = 0

                while (
                    left < len(first_sums)
                    and first_sums[left] == first_value
                ):
                    first_count += 1
                    left += 1

                while (
                    right >= 0
                    and second_sums[right] == second_value
                ):
                    second_count += 1
                    right -= 1

                count += first_count * second_count

        return count


# ============================================================
# OTHER USEFUL SOLUTIONS
# ============================================================


# Approach 4: Sorted Pair Sums + Binary Search
#
# Time Complexity: O(n² log n)
# Space Complexity: O(n²)
#
# Required sum first_sums lo ఎన్నిసార్లు ఉందో
# bisect_left and bisect_right tho calculate chestunnam.

class Solution4:
    def fourSumCount(
        self,
        nums1: List[int],
        nums2: List[int],
        nums3: List[int],
        nums4: List[int]
    ) -> int:

        from bisect import bisect_left, bisect_right

        first_sums = sorted(
            first + second
            for first in nums1
            for second in nums2
        )

        count = 0

        for third in nums3:
            for fourth in nums4:
                required = -(third + fourth)

                left = bisect_left(first_sums, required)
                right = bisect_right(first_sums, required)

                count += right - left

        return count


# ============================================================
# Approach 5: Four Nested Loops
#
# Time Complexity: O(n⁴)
# Space Complexity: O(1)
#
# Brute-force approach.

class Solution5:
    def fourSumCount(
        self,
        nums1: List[int],
        nums2: List[int],
        nums3: List[int],
        nums4: List[int]
    ) -> int:

        count = 0

        for first in nums1:
            for second in nums2:
                for third in nums3:
                    for fourth in nums4:
                        if (
                            first
                            + second
                            + third
                            + fourth
                            == 0
                        ):
                            count += 1

        return count
