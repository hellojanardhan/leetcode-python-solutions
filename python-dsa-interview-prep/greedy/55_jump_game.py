# LeetCode 55 - Jump Game
# Difficulty: Medium

# Recommended Approach:
# Greedy - Farthest Reach
#
# Recommended Current-Level Approach:
# Greedy - Farthest Reach
#
# Main Strategy:
# Greedy
#
# LeetCode Topics:
# Array
# Dynamic Programming
# Greedy


# ============================================================
# TOP APPROACHES
# ============================================================


# Approach 1: Greedy - Farthest Reach
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
# maximum variable:
#
# So far manam maximum ye index varaku
# reach avvagalamo store chestundi.
#
# Initially:
#
# maximum = 0
#
# Enduku?
#
# Manam starting index 0 daggara unnam.
#
#
# Every index i daggara:
#
# First check:
#
# if i > maximum:
#     return False
#
# Meaning:
#
# Current index i,
# mana reachable range kanna mundu undi.
#
# Ante current index ni reach avvaledu.
#
# Current index reach avvakapothe,
# nums[i] value ni use cheyyalem.
#
#
# Current index reachable ayite:
#
# i + nums[i]
#
# calculate chestham.
#
# i:
# current position
#
# nums[i]:
# current position nunchi maximum jump length
#
# i + nums[i]:
# current position nunchi maximum reachable index
#
#
# Then:
#
# maximum = max(
#     maximum,
#     i + nums[i]
# )
#
# Old reachable distance and
# current index reachable distance lo
# bigger value store chestham.
#
#
# Example:
#
# nums = [2, 3, 1, 1, 4]
#
# index:
#  0  1  2  3  4
#
# i = 0
#
# maximum = 0
#
# 0 > 0 ?
# False
#
# maximum =
# max(0, 0 + 2)
# = 2
#
# So indexes:
# 0, 1, 2
# reachable.
#
#
# i = 1
#
# 1 > 2 ?
# False
#
# maximum =
# max(2, 1 + 3)
# = 4
#
# Last index = 4
#
# So last index reachable.
#
#
# Time:
# Each index maximum one time process chestham.
#
# O(n)
#
# Space:
# maximum, n, i variables maatrame.
#
# O(1).

class Solution1:
    def canJump(self, nums: list[int]) -> bool:
        maximum = 0
        n = len(nums)

        for i in range(n):

            if i > maximum:
                return False

            maximum = max(
                maximum,
                i + nums[i]
            )

        return True


# ============================================================


# Approach 2: Greedy - Backward Goal
# Recommended Optimal Alternative
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
# Approach 1 lo:
#
# left -> right
#
# farthest reachable index track chestham.
#
# Ee approach lo reverse thinking:
#
# right -> left
#
# Current goal ni reach cheyyagalige
# previous index ni search chestham.
#
#
# Initially:
#
# goal = last index
#
# Example:
#
# nums = [2, 3, 1, 1, 4]
#
# last index:
# goal = 4
#
#
# Right nunchi left ki traverse chestham.
#
# Oka index i nunchi goal reach cheyyagalama?
#
# Condition:
#
# i + nums[i] >= goal
#
# True ayite:
#
# goal = i
#
# Meaning:
#
# Original goal ni reach cheyyadaniki
# ippudu index i reach ayite chaalu.
#
#
# Example:
#
# goal = 4
#
# i = 3
# nums[3] = 1
#
# 3 + 1 >= 4
#
# True
#
# So:
#
# goal = 3
#
#
# i = 2
#
# 2 + 1 >= 3
#
# True
#
# goal = 2
#
#
# i = 1
#
# 1 + 3 >= 2
#
# True
#
# goal = 1
#
#
# i = 0
#
# 0 + 2 >= 1
#
# True
#
# goal = 0
#
#
# Final goal == 0
#
# Ante starting index nunchi
# last index reachable.
#
# Return True.
#
#
# Time:
# One reverse traversal.
#
# O(n)
#
# Space:
# goal variable only.
#
# O(1).

class Solution2:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1

        for i in range(
            len(nums) - 2,
            -1,
            -1
        ):

            if i + nums[i] >= goal:
                goal = i

        return goal == 0


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 3: Dynamic Programming
# Pattern:
# Array + Dynamic Programming
#
# Not Recommended Over Greedy
#
# Time Complexity:
# O(n^2)
#
# Space Complexity:
# O(n)
#
# Time Explanation:
# dp[i] meaning:
#
# index i reachable aa?
#
# Initially:
#
# dp[0] = True
#
# because manam index 0 daggara start chestham.
#
#
# Every reachable index i nunchi,
# nums[i] range lo unna next indexes ni
# reachable ga mark chestham.
#
#
# Example:
#
# nums = [2, 3, 1, 1, 4]
#
# Initially:
#
# dp =
# [True, False, False, False, False]
#
#
# i = 0
#
# nums[0] = 2
#
# So:
#
# index 1 reachable
# index 2 reachable
#
# dp =
# [True, True, True, False, False]
#
#
# i = 1
#
# nums[1] = 3
#
# Reach:
#
# index 2
# index 3
# index 4
#
# dp =
# [True, True, True, True, True]
#
# Last index True.
#
#
# Worst case lo every index nunchi
# many next indexes check cheyyachu.
#
# Kabatti:
#
# O(n^2)
#
# Space:
# dp array size n.
#
# O(n).
#
# Greedy O(n) kabatti
# interview lo Greedy better.

class Solution3:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)

        dp = [False] * n
        dp[0] = True

        for i in range(n):

            if not dp[i]:
                continue

            farthest = min(
                n - 1,
                i + nums[i]
            )

            for j in range(
                i + 1,
                farthest + 1
            ):
                dp[j] = True

        return dp[n - 1]


# ============================================================
# PATTERN SUMMARY
# ============================================================


# Array:
# Input array lo index and value relationship
# main role play chestundi.
#
# index:
# current position
#
# nums[index]:
# maximum jump length
#
# index + nums[index]:
# maximum reachable index
#
#
# Greedy - Forward:
#
# So far maximum reachable index ni
# track chestham.
#
# Formula:
#
# maximum = max(
#     maximum,
#     i + nums[i]
# )
#
# If:
#
# i > maximum
#
# current index unreachable.
#
# Return False.
#
#
# Greedy - Backward:
#
# Last index ni goal ga petti,
# goal ni reach cheyyagalige
# earliest previous indexes ki
# goal ni move chestham.
#
# Condition:
#
# i + nums[i] >= goal
#
#
# Dynamic Programming:
#
# Each index reachable aa kaada
# dp array lo store chestham.
#
# Valid approach,
# but O(n^2).
#
#
# ============================================================
# BEST INTERVIEW CHOICE
# ============================================================
#
# Greedy - Farthest Reach
#
# Time:
# O(n)
#
# Space:
# O(1)
#
# Nee current solution exactly ide.
