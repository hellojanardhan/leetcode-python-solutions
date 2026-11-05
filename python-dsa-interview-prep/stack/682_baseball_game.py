# ============================================================
# LEETCODE 682 - BASEBALL GAME
# Difficulty: Easy
#
# Recommended Approach: Stack + Simulation
# Recommended Current-Level Approach: Stack + Simulation
#
# n = Total number of operations.
#
# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Stack + Simulation
# Your Approach — cleaned
# Recommended Optimal Approach
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Logic:
# Prathi operation ni process chestham.
#
# Integer:
# Score ni stack lo push chestham.
#
# C:
# Previous score ni remove chestham.
#
# D:
# Previous score double chesi push chestham.
#
# +:
# Last two scores add chesi push chestham.
#
# Final ga stack lo unna scores sum return chestham.

class Solution1:
    def calPoints(self, operations: list[str]) -> int:
        stack = []

        for operation in operations:
            if operation not in ("C", "D", "+"):
                stack.append(int(operation))

            elif operation == "C":
                stack.pop()

            elif operation == "D":
                stack.append(2 * stack[-1])

            elif operation == "+":
                stack.append(stack[-1] + stack[-2])

        return sum(stack)


# ============================================================


# Approach 2: Stack + If-Elif with Integer Conversion
# Alternative Approach
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Logic:
# Operation special command kaakapothe integer ga convert chestham.
# Special commands ki separate conditions use chestham.
#
# Advantage:
# Your original code structure ki close ga untundi.

class Solution2:
    def calPoints(self, operations: list[str]) -> int:
        answer = []

        for operation in operations:
            if operation == "C":
                answer.pop()

            elif operation == "D":
                answer.append(2 * answer[-1])

            elif operation == "+":
                answer.append(answer[-1] + answer[-2])

            else:
                answer.append(int(operation))

        return sum(answer)


# ============================================================


# Approach 3: Stack + Running Total
# Alternative Approach
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Logic:
# Stack lo scores maintain chestham.
# Along with stack, total score ni maintain chestham.
#
# C:
# Removed score ni total nunchi subtract chestham.
#
# D:
# Double score ni total ki add chestham.
#
# +:
# Last two scores sum ni total ki add chestham.
#
# Advantage:
# Final ga sum(stack) traverse cheyyalsina avasaram ledu.

class Solution3:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        total = 0

        for operation in operations:
            if operation == "C":
                removed = stack.pop()
                total -= removed

            elif operation == "D":
                score = 2 * stack[-1]
                stack.append(score)
                total += score

            elif operation == "+":
                score = stack[-1] + stack[-2]
                stack.append(score)
                total += score

            else:
                score = int(operation)
                stack.append(score)
                total += score

        return total


# ============================================================
# COMPLEXITY COMPARISON
# ============================================================
#
# Approach 1:
# Time O(n), Space O(n)
#
# Approach 2:
# Time O(n), Space O(n)
#
# Approach 3:
# Time O(n), Space O(n)
#
# All approaches are asymptotically optimal.
# Approach 3 avoids the final O(n) sum traversal,
# but overall time complexity remains O(n).


# ============================================================
# DETAILED DRY RUN - APPROACH 1
# ============================================================
#
# Input:
#
# operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]
#
# STEP 1: "5"
# Push 5
# Stack: [5]
#
# STEP 2: "-2"
# Push -2
# Stack: [5, -2]
#
# STEP 3: "4"
# Push 4
# Stack: [5, -2, 4]
#
# STEP 4: "C"
# Remove 4
# Stack: [5, -2]
#
# STEP 5: "D"
# Double previous score: -2 * 2 = -4
# Stack: [5, -2, -4]
#
# STEP 6: "9"
# Push 9
# Stack: [5, -2, -4, 9]
#
# STEP 7: "+"
# Add last two: 9 + (-4) = 5
# Stack: [5, -2, -4, 9, 5]
#
# STEP 8: "+"
# Add last two: 5 + 9 = 14
# Stack: [5, -2, -4, 9, 5, 14]
#
# Final sum:
# 5 - 2 - 4 + 9 + 5 + 14 = 27
#
# Expected Output: 27


# ============================================================
# IMPORTANT TEST CASES
# ============================================================
#
# Test 1:
# ["5", "2", "C", "D", "+"]
# Output: 30
#
# Test 2:
# ["5", "-2", "4", "C", "D", "9", "+", "+"]
# Output: 27
#
# Test 3:
# ["1", "2", "+"]
# Output: 4
#
# Test 4:
# ["-5", "-10", "D"]
# Output: -35
#
# Test 5:
# ["10", "C"]
# Output: 0


# ============================================================
# INTERVIEW-READY EXPLANATION
# ============================================================
#
# "I solved the Baseball Game problem using a stack.
#
# I traverse the operations one by one.
# If the operation is an integer, I push it onto the stack.
#
# If it is C, I remove the previous score.
# If it is D, I push double the previous score.
# If it is +, I push the sum of the previous two scores.
#
# Finally, I return the sum of all valid scores.
#
# Each operation is processed once, so the time complexity
# is O(n), and the auxiliary space complexity is O(n)."


# ============================================================
# FINAL RECOMMENDATION
# ============================================================
#
# Recommended: Approach 1 or Approach 2.
#
# Both are simple, readable and optimal.
# Approach 3 is useful to understand running totals.
#
# ============================================================
# FILENAME
# ============================================================
#
# 682_baseball_game.py
#
# ============================================================
