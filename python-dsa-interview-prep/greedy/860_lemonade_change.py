# LeetCode 860 - Lemonade Change
# Difficulty: Easy

# Recommended Approach:
# Greedy + Denomination Tracking
#
# Recommended Current-Level Approach:
# Greedy + Count $5 and $10 Bills
#
# Main Strategy:
# Greedy


# ============================================================
# TOP APPROACHES
# ============================================================


# Approach 1: Greedy + Denomination Tracking
# Your Approach
# Recommended Current-Level Approach
# Recommended Optimal Approach
#
# Pattern:
# Greedy
#
# Time Complexity:
# O(n)
#
# Space Complexity:
# O(1)
#
# Time Explanation:
# Customers ni left-to-right process chestunnam.
#
# Prati customer bill:
# $5, $10, or $20.
#
#
# bill == 5:
#
# Customer exact amount ichadu.
# Change ivvalsina avasaram ledu.
#
# So:
#
# count_5 += 1
#
#
# ------------------------------------------------------------
#
# bill == 10:
#
# Lemonade price = $5.
#
# Customer $10 ichadu.
#
# Change:
#
# 10 - 5 = 5
#
# Kabatti one $5 bill kavali.
#
# If:
#
# count_5 == 0
#
# change ivvalemu.
#
# return False.
#
# Otherwise:
#
# count_5 -= 1
#
# Customer ichina $10 bill ni store chestham:
#
# count_10 += 1
#
#
# ------------------------------------------------------------
#
# bill == 20:
#
# Customer ki:
#
# 20 - 5 = 15
#
# change ivvali.
#
# $15 ni two main ways lo ivvachu:
#
# $10 + $5
#
# OR
#
# $5 + $5 + $5
#
#
# First preference:
#
# $10 + $5
#
# Enduku?
#
# $5 bills future $10 customers ki
# compulsory ga kavali.
#
# So possible ayite:
#
# one $10 bill
# +
# one $5 bill
#
# use chestham.
#
# This preserves more $5 bills.
#
#
# If $10 bill lekapothe:
#
# at least 3 $5 bills unnaya ani check chestham.
#
# count_5 >= 3
#
# ayite:
#
# count_5 -= 3
#
#
# Rendu possibilities lekapothe:
#
# return False.
#
#
# ------------------------------------------------------------
#
# Example:
#
# bills = [5, 5, 5, 10, 20]
#
# Start:
#
# count_5 = 0
# count_10 = 0
#
#
# bill = 5
#
# count_5 = 1
#
#
# bill = 5
#
# count_5 = 2
#
#
# bill = 5
#
# count_5 = 3
#
#
# bill = 10
#
# Need $5 change.
#
# count_5 = 2
# count_10 = 1
#
#
# bill = 20
#
# Need $15 change.
#
# We have:
#
# one $10
# and
# two $5 bills
#
# Prefer:
#
# $10 + $5
#
# So:
#
# count_10 = 0
# count_5 = 1
#
# All customers served.
#
# return True.
#
#
# Time:
# Each bill only once process chestham.
#
# O(n)
#
# Space:
# count_5 and count_10 only.
#
# O(1).

class Solution1:
    def lemonadeChange(
        self,
        bills: list[int]
    ) -> bool:

        count_5 = 0
        count_10 = 0

        for bill in bills:

            if bill == 5:
                count_5 += 1

            elif bill == 10:
                count_10 += 1

                if count_5 == 0:
                    return False

                count_5 -= 1

            elif bill == 20:

                if count_5 and count_10:
                    count_5 -= 1
                    count_10 -= 1

                elif count_5 >= 3:
                    count_5 -= 3

                else:
                    return False

        return True


# ============================================================
# IMPORTANT GREEDY DECISION
# ============================================================


# For $20:
#
# Why choose:
#
# $10 + $5
#
# before:
#
# $5 + $5 + $5 ?
#
#
# Example:
#
# Suppose:
#
# count_5 = 3
# count_10 = 1
#
# Customer gives $20.
#
#
# Option 1:
#
# Give:
# $10 + $5
#
# Remaining:
#
# count_5 = 2
# count_10 = 0
#
#
# Option 2:
#
# Give:
# $5 + $5 + $5
#
# Remaining:
#
# count_5 = 0
# count_10 = 1
#
#
# If next customer gives $10:
#
# We MUST give one $5.
#
# Option 2 lo $5 bills levu.
#
# So fail avvachu.
#
# Kabatti greedy choice:
#
# Preserve $5 bills as much as possible.
#
# For $20:
#
# Prefer:
# $10 + $5
#
# Then only:
# $5 + $5 + $5


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# There is no better meaningful interview approach
# than this Greedy O(n), O(1) solution.
#
# Brute-force / backtracking possible,
# but unnecessary and inefficient.
#
# So TOP APPROACHES lo
# same greedy logic ni different names tho
# repeat cheyyalsina avasaram ledu.


# ============================================================
# PATTERN SUMMARY
# ============================================================


# $5:
# Keep it.
#
#
# $10:
# Need one $5.
#
#
# $20:
# Need $15.
#
# First:
# $10 + $5
#
# Otherwise:
# $5 + $5 + $5
#
#
# Main Greedy Rule:
#
# Preserve $5 bills whenever possible.
#
#
# Best Interview Approach:
#
# Greedy + Denomination Tracking
#
# Time:
# O(n)
#
# Space:
# O(1)
