# LeetCode 605 - Can Place Flowers
# Difficulty: Easy

# Recommended Approach:
# Greedy + Array Traversal
#
# Recommended Current-Level Approach:
# Greedy + Left/Right Neighbor Check
#
# Main Strategy:
# Greedy
#
# LeetCode Topics:
# Array
# Greedy


# ============================================================
# TOP APPROACHES
# ============================================================


# Approach 1: Greedy + Left/Right Neighbor Check
# Your Approach
# Recommended Current-Level Approach
# Recommended Optimal Approach
#
# Pattern:
# Array + Greedy
#
# Time Complexity:
# O(n)
#
# Space Complexity:
# O(1)
#
# Time Explanation:
# Flowerbed ni left nunchi right varaku
# one time traverse chestunnam.
#
# Prati index i daggara first:
#
# flowerbed[i] == 0
#
# ani check chestunnam.
#
# Current position empty ayitene
# new flower plant cheyyadam possible.
#
# Tarvata left side safe aa ani check chestham:
#
# left = (i == 0)
#        OR
#        flowerbed[i - 1] == 0
#
# i == 0 ante:
# first index.
#
# First index ki left neighbor undadu.
# Kabatti automatically left safe.
#
# Otherwise:
# left neighbor 0 undali.
#
#
# Same way right side:
#
# right = (i == length - 1)
#         OR
#         flowerbed[i + 1] == 0
#
# Last index ki right neighbor undadu,
# kabatti automatically safe.
#
# Otherwise:
# right neighbor 0 undali.
#
#
# If:
#
# current == 0
# AND
# left safe
# AND
# right safe
#
# appudu flower plant cheyochu.
#
# flowerbed[i] = 1
#
# ani immediately array update chestunnam.
#
# Idi very important.
#
# Enduku?
#
# Next indexes process chestunnappudu
# newly planted flower ni kuda
# neighbor ga consider cheyyali.
#
# Tarvata:
#
# n -= 1
#
# Required flowers anni plant ayite:
#
# n == 0
#
# immediate ga True return chestham.
#
# Entire array scan ayyaka kuda
# n > 0 unte:
#
# return False
#
#
# Example:
#
# flowerbed = [0, 0, 0, 0, 1]
# n = 2
#
# i = 0
#
# current = 0
# left = True
# right = True
#
# Plant:
#
# [1, 0, 0, 0, 1]
#
# n = 1
#
#
# i = 1
#
# current = 0
# left = 1
#
# Cannot plant.
#
#
# i = 2
#
# left = 0
# current = 0
# right = 0
#
# Plant:
#
# [1, 0, 1, 0, 1]
#
# n = 0
#
# return True
#
#
# Time:
# One traversal only.
#
# O(n)
#
# Space:
# Few variables only.
#
# O(1)

class Solution1:
    def canPlaceFlowers(
        self,
        flowerbed: list[int],
        n: int
    ) -> bool:

        if n == 0:
            return True

        length = len(flowerbed)

        for i in range(length):

            if flowerbed[i] == 0:

                left = (
                    i == 0
                    or flowerbed[i - 1] == 0
                )

                right = (
                    i == length - 1
                    or flowerbed[i + 1] == 0
                )

                if left and right:
                    flowerbed[i] = 1
                    n -= 1

                    if n == 0:
                        return True

        return False


# ============================================================


# Approach 2: Greedy + Zero Segment Counting
# Recommended Alternative Approach
#
# Pattern:
# Array + Greedy + Gap Counting
#
# Time Complexity:
# O(n)
#
# Space Complexity:
# O(1)
#
# Time Explanation:
# Ee approach lo every position lo
# flower actually place cheyyamu.
#
# Instead consecutive zero segments
# length ni count chestham.
#
# Example:
#
# [1, 0, 0, 0, 0, 0, 1]
#
# Middle zero segment:
#
# 0 0 0 0 0
#
# length = 5
#
# Both sides flowers unnayi.
#
# So available positions:
#
# indexes:
# 1 2 3 4 5
#
# first and last zero positions
# existing flowers ki adjacent ga unnayi.
#
# Actual usable pattern:
#
# 0 1 0 1 0
#
# So 2 new flowers place cheyochu.
#
#
# Boundary zero segments different ga
# handle cheyyali.
#
# Example:
#
# [0, 0, 0, 0, 1]
#
# Left boundary lo flower ledu.
#
# So first position ni use cheyochu.
#
# Maximum placements:
#
# [1, 0, 1, 0, 1]
#
# = 2
#
#
# Ee approach kuda O(n),
# but boundary formulas careful ga
# handle cheyyali.
#
# Interview lo Approach 1
# simpler and safer.

class Solution2:
    def canPlaceFlowers(
        self,
        flowerbed: list[int],
        n: int
    ) -> bool:

        length = len(flowerbed)
        possible = 0
        i = 0

        while i < length:

            if flowerbed[i] == 1:
                i += 1
                continue

            start = i

            while (
                i < length
                and flowerbed[i] == 0
            ):
                i += 1

            zeros = i - start

            left_flower = (
                start > 0
                and flowerbed[start - 1] == 1
            )

            right_flower = (
                i < length
                and flowerbed[i] == 1
            )

            if left_flower and right_flower:
                possible += (zeros - 1) // 2

            elif left_flower or right_flower:
                possible += zeros // 2

            else:
                possible += (zeros + 1) // 2

            if possible >= n:
                return True

        return possible >= n


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 3: Try Planting + Full Validation
# Brute Force / Simulation
# Not Recommended
#
# Pattern:
# Array + Simulation
#
# Time Complexity:
# O(n^2)
#
# Space Complexity:
# O(1)
#
# Time Explanation:
# Prati empty position lo temporary ga
# flower plant chestham.
#
# Tarvata entire flowerbed ni
# malli scan chesi adjacent 1,1
# unnaya ani validate chestham.
#
# Valid ayite placement keep chestham.
#
# Invalid ayite:
#
# flowerbed[i] = 0
#
# ani undo chestham.
#
# Outer loop:
# O(n)
#
# Full validation:
# O(n)
#
# Total:
# O(n^2)
#
# Ee approach work avvachu,
# kani unnecessary repeated scanning chestundi.
#
# Approach 1 same decision ni
# local neighbors check chesi
# O(n) lo solve chestundi.

class Solution3:
    def canPlaceFlowers(
        self,
        flowerbed: list[int],
        n: int
    ) -> bool:

        if n == 0:
            return True

        length = len(flowerbed)
        count = 0

        for i in range(length):

            if flowerbed[i] == 0:

                flowerbed[i] = 1
                valid = True

                for j in range(length - 1):

                    if (
                        flowerbed[j] == 1
                        and flowerbed[j + 1] == 1
                    ):
                        valid = False
                        break

                if valid:
                    count += 1
                else:
                    flowerbed[i] = 0

                if count >= n:
                    return True

        return False


# ============================================================
# PATTERN SUMMARY
# ============================================================


# Array:
# Flowerbed ni sequential ga traverse chestham.
#
#
# Greedy:
# Left-to-right scan lo
# earliest valid position kanipinchagane
# flower plant chestham.
#
# Earliest valid position ni choose cheyyadam valla
# right side lo maximum space preserve avutundi.
#
#
# Main condition:
#
# Current = 0
#
# AND
#
# Left =
# 0 OR doesn't exist
#
# AND
#
# Right =
# 0 OR doesn't exist
#
#
# Then:
#
# flowerbed[i] = 1
# n -= 1
#
#
# Recommended Interview Approach:
#
# Greedy
# +
# Left/Right Neighbor Check
#
#
# Time:
# O(n)
#
# Space:
# O(1)
