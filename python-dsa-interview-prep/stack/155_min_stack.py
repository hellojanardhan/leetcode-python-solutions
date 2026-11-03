# ============================================================
# LEETCODE 155 - MIN STACK
# Difficulty: Medium
#
# Recommended Approach: Single Stack + Running Minimum
# Recommended Current-Level Approach: Single Stack + Running Minimum
#
# n = total number of elements pushed into the stack.
#
# All stack operations take O(1) time.
# ============================================================


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Single Stack + Running Minimum
# Your Approach — cleaned
# Recommended Optimal Approach
#
# Time Complexity:
# push()    : O(1)
# pop()     : O(1)
# top()     : O(1)
# getMin()  : O(1)
#
# Space Complexity: O(n)
#
# Logic:
# Prathi element ni (value, current_min) tuple ga store chestham.
#
# First element ayithe (value, value) store chestham.
# Next elements push chesetappudu:
# Previous minimum tho current value compare chestham.
# Minimum value ni tuple lo store chestham.
#
# stack[-1][0] -> Top element
# stack[-1][1] -> Current minimum
#
# Advantage:
# Minimum value ni direct ga access cheyochu.
# Entire stack traverse cheyyalsina avasaram ledu.

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append((value, value))
        else:
            current_min = min(value, self.stack[-1][1])
            self.stack.append((value, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# ============================================================


# Approach 2: Two Stacks
# Alternative Approach
#
# Time Complexity:
# push()    : O(1)
# pop()     : O(1)
# top()     : O(1)
# getMin()  : O(1)
#
# Space Complexity: O(n)
#
# Logic:
# Two separate stacks maintain chestham.
#
# Main stack:
# Actual values store chestham.
#
# Min stack:
# Prathi position ki current minimum store chestham.
#
# Push:
# Main stack lo value append chestham.
# Min stack empty ayithe value append chestham.
# Leda previous minimum and current value lo minimum append chestham.
#
# Pop:
# Rendu stacks nunchi top elements remove chestham.
#
# getMin:
# Min stack top return chestham.

class MinStack2:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.min_stack:
            self.min_stack.append(value)
        else:
            current_min = min(value, self.min_stack[-1])
            self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# ============================================================


# Approach 3: Single Stack + Encoded Values
# Advanced Alternative
#
# Time Complexity:
# push()    : O(1)
# pop()     : O(1)
# top()     : O(1)
# getMin()  : O(1)
#
# Space Complexity: O(n)
#
# Logic:
# Separate minimum stack avasaram ledu.
# Single stack lo actual values and encoded values store chestham.
#
# First element:
# Stack lo value push chestham.
# min_value initialize chestham.
#
# New value current minimum kanna chinnadi ayithe:
# Encoded value = 2 * value - min_value
# Encoded value stack lo push chestham.
# min_value ni new value tho update chestham.
#
# Pop:
# Top encoded value current minimum kanna chinnadi ayithe,
# previous minimum ni decode chestham:
#
# previous_min = 2 * min_value - encoded_value
#
# Top:
# Top value encoded ayithe actual minimum return chestham.
# Leda top value ne return chestham.
#
# Note:
# Idi advanced mathematical approach.
# Interview lo logic explain cheyyadam konchem difficult.

class MinStack3:

    def __init__(self):
        self.stack = []
        self.min_value = None

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append(value)
            self.min_value = value

        elif value >= self.min_value:
            self.stack.append(value)

        else:
            encoded_value = 2 * value - self.min_value
            self.stack.append(encoded_value)
            self.min_value = value

    def pop(self) -> None:
        top_value = self.stack.pop()

        if top_value < self.min_value:
            self.min_value = 2 * self.min_value - top_value

        if not self.stack:
            self.min_value = None

    def top(self) -> int:
        top_value = self.stack[-1]

        if top_value < self.min_value:
            return self.min_value

        return top_value

    def getMin(self) -> int:
        return self.min_value


# ============================================================
# OTHER USEFUL SOLUTIONS
# ============================================================


# Approach 4: Brute Force - Single Normal Stack
#
# Time Complexity:
# push()    : O(1)
# pop()     : O(1)
# top()     : O(1)
# getMin()  : O(n)
#
# Space Complexity: O(n)
#
# Logic:
# Normal stack lo actual values matrame store chestham.
# getMin() call chesinappudu entire stack lo minimum find chestham.
#
# Advantage:
# Simple implementation.
#
# Disadvantage:
# getMin() takes O(n), so problem requirement meet kaadu.

class MinStack4:

    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


# ============================================================
# COMPLEXITY COMPARISON
# ============================================================
#
# Approach 1: Tuple Stack
# Push O(1), Pop O(1), Top O(1), GetMin O(1)
# Space O(n)
#
# Approach 2: Two Stacks
# Push O(1), Pop O(1), Top O(1), GetMin O(1)
# Space O(n)
#
# Approach 3: Encoded Single Stack
# Push O(1), Pop O(1), Top O(1), GetMin O(1)
# Space O(n)
#
# Approach 4: Brute Force
# Push O(1), Pop O(1), Top O(1), GetMin O(n)
# Space O(n)


# ============================================================
# DETAILED DRY RUN - APPROACH 1
# ============================================================
#
# Operations:
#
# push(-2)
# push(0)
# push(-3)
# getMin()
# pop()
# top()
# getMin()
#
# STEP 1: push(-2)
#
# Stack:
# [(-2, -2)]
#
# Current minimum = -2
#
# STEP 2: push(0)
#
# current_min = min(0, -2)
#             = -2
#
# Stack:
# [(-2, -2), (0, -2)]
#
# Current minimum = -2
#
# STEP 3: push(-3)
#
# current_min = min(-3, -2)
#             = -3
#
# Stack:
# [(-2, -2), (0, -2), (-3, -3)]
#
# Current minimum = -3
#
# STEP 4: getMin()
#
# Returns -3
#
# STEP 5: pop()
#
# Removes (-3, -3)
#
# Stack:
# [(-2, -2), (0, -2)]
#
# STEP 6: top()
#
# Returns 0
#
# STEP 7: getMin()
#
# Returns -2
#
# Expected Output:
# [-3, 0, -2]


# ============================================================
# IMPORTANT TEST CASES
# ============================================================
#
# Test Case 1: Normal values
#
# push(5)
# push(3)
# push(7)
# getMin() -> 3
#
# Test Case 2: Negative values
#
# push(-2)
# push(-5)
# push(-1)
# getMin() -> -5
#
# Test Case 3: Duplicate minimum
#
# push(2)
# push(1)
# push(1)
# pop()
# getMin() -> 1
#
# Test Case 4: Minimum changes after pop
#
# push(10)
# push(5)
# push(2)
# pop()
# getMin() -> 5
#
# Test Case 5: Single element
#
# push(4)
# getMin() -> 4
# top() -> 4


# ============================================================
# INTERVIEW-READY EXPLANATION
# ============================================================
#
# "I implemented Min Stack using a single stack with a running
# minimum.
#
# Instead of storing only the actual value, I store each element
# as a tuple containing the value and the minimum value up to
# that position.
#
# Whenever I push a new element, I compare it with the previous
# minimum and store the smaller value.
#
# This allows me to retrieve the minimum directly from the top
# of the stack without traversing the entire stack.
#
# Therefore, push, pop, top, and getMin all take O(1) time,
# with O(n) auxiliary space."


# ============================================================
# FINAL RECOMMENDATION
# ============================================================
#
# Recommended: Approach 1 - Tuple Stack
#
# Reason:
# Easy to understand.
# Easy to implement.
# All operations O(1).
# No complicated decoding logic.
#
# Approach 2 is also a good interview alternative.
# Approach 3 is useful as an advanced concept.
#
# ============================================================
# FILENAME
# ============================================================
#
# 155_min_stack.py
#
# ============================================================
