# ============================================================
# LeetCode 1004: Max Consecutive Ones III
# Difficulty: Medium
# Topic: Sliding Window, Two Pointers
# ============================================================

"""
PROBLEM:
Given a binary array nums and an integer k, you can flip at
most k zeros to ones.

Return the maximum number of consecutive ones in the array
after performing at most k flips.

Example:
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

Output: 6

Explanation:
Flip the zeros at indices 4 and 5.
The longest valid subarray has length 6.
"""


# ============================================================
# RECOMMENDED OPTIMAL APPROACH
# ============================================================

"""
Sliding Window — Two Pointers

Time Complexity: O(n)
Space Complexity: O(1)

WHY THIS IS OPTIMAL:
- Right pointer r expand chestundi.
- Zero encounter ayithe zeros count increase chestham.
- Zeros > k ayithe left pointer l move chestham.
- Valid window unnapudu maximum length update chestham.
- Each pointer maximum n times move avuthundi.

IMPORTANT:
Your accepted IF-based solution is a valid optimization.
It does not always shrink the window until it is immediately
valid. Instead, it moves left by one position whenever the
zero count exceeds k and updates max_length only for valid
windows. This is sufficient for finding the maximum length.
"""


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# ------------------------------------------------------------
# SOLUTION 1: BRUTE FORCE
# ------------------------------------------------------------

"""
Approach:
Prathi starting index i nunchi subarray extend chestham.
Zeros count maintain chestham.
Zeros > k ayithe further extend cheyyalsina avasaram ledu.
Valid subarray length calculate chesi maximum update chestham.

Time Complexity: O(n^2)
Space Complexity: O(1)

Best for:
- Understanding the problem
- Learning brute-force enumeration
- Small input sizes
"""

class BruteForceSolution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_length = 0

        for i in range(len(nums)):
            zeros = 0

            for j in range(i, len(nums)):
                if nums[j] == 0:
                    zeros += 1

                if zeros > k:
                    break

                length = j - i + 1
                max_length = max(max_length, length)

        return max_length


# LOGIC:
# i = starting index
# j = ending index
# zeros = current subarray lo unna zeros
# length = j - i + 1
#
# Example:
# nums = [1, 0, 1, 1, 0]
# k = 1
#
# Starting index 0:
# [1]       -> zeros = 0, length = 1
# [1, 0]    -> zeros = 1, length = 2
# [1, 0, 1] -> zeros = 1, length = 3
# [1, 0, 1, 1] -> zeros = 1, length = 4
# Next element is 0 -> zeros = 2 > k, break.
#
# Maximum valid length = 4


# ------------------------------------------------------------
# SOLUTION 2: SLIDING WINDOW USING WHILE
# ------------------------------------------------------------

"""
Approach:
Window lo zeros k kanna ekkuva ayithe, window valid ayye
varaku left pointer move chestham.

Time Complexity: O(n)
Space Complexity: O(1)

Advantage:
- Window validity explicitly maintain chestham.
- Interview lo explain cheyyadaniki straightforward.
"""

class SlidingWindowWhileSolution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zeros = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1

                left += 1

            length = right - left + 1
            max_length = max(max_length, length)

        return max_length


# LOGIC:
# 1. Right pointer window expand chestundi.
# 2. Zero vachinappudu zeros += 1.
# 3. zeros > k ayithe left side nunchi elements remove chestham.
# 4. Left element zero ayithe zeros -= 1.
# 5. Window valid ayyaka length calculate chestham.
#
# Window valid condition:
# zeros <= k
#
# Window length:
# right - left + 1
#
# Prathi element maximum once add and once remove avuthundi.
# Anduke total time O(n).


# ------------------------------------------------------------
# SOLUTION 3: OPTIMIZED SLIDING WINDOW USING IF
# YOUR ACCEPTED SOLUTION
# ------------------------------------------------------------

"""
Approach:
zeros > k ayinappudu left pointer ni only one position move
chestham. Left element zero ayithe zero count decrease chestham.

Window temporary ga invalid ga undochu.
Kani invalid window length ni maximum ga update cheyyam.

Ee problem lo maximum length kosam ee optimization work avuthundi.

Time Complexity: O(n)
Space Complexity: O(1)

This is your accepted approach.
"""

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_length = 0
        r = 0
        l = 0
        zeros = 0

        while r < len(nums):
            if nums[r] == 0:
                zeros += 1

            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            if zeros <= k:
                length = r - l + 1
                max_length = max(max_length, length)

            r += 1

        return max_length


# WHY YOUR IF APPROACH WORKS:
#
# Normally, while approach invalid window ni valid ayye varaku
# shrink chestundi.
#
# Your approach:
# - Invalid ayithe left pointer one step move chestundi.
# - Valid ayithe maximum length update chestundi.
# - Invalid ayithe maximum length update cheyyadu.
#
# Ee approach lo window size decrease avvakunda maintain avuthundi
# (or same size lo untundi) as right moves forward.
# Invalid windows maximum answer ni update cheyyavu.
#
# Therefore, maximum valid length correct ga track avuthundi.
#
# IMPORTANT:
# This reasoning is specific to finding the maximum length.
# Similar-looking problems lo, exact valid window or window
# counts kavali ante, one-step IF replacement always sufficient
# ani assume cheyyakudadhu.


# ============================================================
# OTHER USEFUL SOLUTION
# ============================================================


# ------------------------------------------------------------
# SOLUTION 4: PREFIX SUM + BINARY SEARCH
# ------------------------------------------------------------

"""
Approach:
Prefix sum array lo zeros count store chestham.

prefix[i] = nums[0:i] lo zeros count

Oka starting index i ki, maximum valid ending index find
cheyyadaniki binary search use chestham.

Time Complexity: O(n log n)
Space Complexity: O(n)

Note:
Idi meaningful alternative, but sliding window O(n) better.
"""

from bisect import bisect_right


class PrefixSumBinarySearchSolution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 - nums[i])

        max_length = 0

        for left in range(n):
            # Right-exclusive endpoint:
            # prefix[right] - prefix[left] <= k
            target = prefix[left] + k

            right = bisect_right(prefix, target, left + 1, n + 1) - 1

            length = right - left
            max_length = max(max_length, length)

        return max_length


# ============================================================
# DETAILED DRY RUN — YOUR ACCEPTED IF SOLUTION
# ============================================================

"""
Input:
nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 3

Initial:
l = 0
r = 0
zeros = 0
max_length = 0

Important window updates:

r = 0:
nums[0] = 0
zeros = 1
Window [0:0] -> length 1
max_length = 1

r = 1:
nums[1] = 0
zeros = 2
Window [0:1] -> length 2
max_length = 2

r = 2:
nums[2] = 1
zeros = 2
Window length = 3
max_length = 3

r = 3:
nums[3] = 1
zeros = 2
Window length = 4
max_length = 4

r = 4:
nums[4] = 0
zeros = 3
Window length = 5
max_length = 5

r = 5:
nums[5] = 0
zeros = 4 > k

nums[l] = nums[0] = 0
zeros becomes 3
l becomes 1

Current window length = 5
max_length = 5

r = 6:
nums[6] = 1
zeros = 3
Window length = 6
max_length = 6

r = 7:
nums[7] = 1
zeros = 3
Window length = 7
max_length = 7

r = 8:
nums[8] = 1
zeros = 3
Window length = 8
max_length = 8

r = 9:
nums[9] = 0
zeros = 4 > k

nums[l] = nums[1] = 0
zeros becomes 3
l becomes 2

Window length = 8
max_length = 8

r = 10:
nums[10] = 1
zeros = 3
Window length = 9
max_length = 9

r = 11:
nums[11] = 1
zeros = 3
Window length = 10
max_length = 10

At r = 12, 13, 14:
The zero count exceeds k.
Left pointer moves one step per iteration.
When the left element is zero, zeros count decreases.

The algorithm continues through the remaining ones.

Final answer:
10
"""


# ============================================================
# TEST CASES
# ============================================================

"""
Test Case 1:
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
Expected Output: 6

Test Case 2:
nums = [0, 0, 0, 1]
k = 0
Expected Output: 1

Test Case 3:
nums = [0, 0, 0, 1]
k = 3
Expected Output: 4

Test Case 4:
nums = [1, 1, 1, 1]
k = 0
Expected Output: 4

Test Case 5:
nums = [0, 0, 0]
k = 0
Expected Output: 0

Test Case 6:
nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 3
Expected Output: 10

Test Case 7:
nums = [1]
k = 0
Expected Output: 1

Test Case 8:
nums = [0]
k = 1
Expected Output: 1
"""


# ============================================================
# COMPLEXITY COMPARISON
# ============================================================

"""
Solution 1: Brute Force
Time:  O(n^2) worst case
Space: O(1)

Solution 2: Sliding Window with WHILE
Time:  O(n)
Space: O(1)

Solution 3: Sliding Window with IF — Your Solution
Time:  O(n)
Space: O(1)

Solution 4: Prefix Sum + Binary Search
Time:  O(n log n)
Space: O(n)


FINAL RECOMMENDATION:
- For understanding: Brute Force
- For standard interview explanation: Sliding Window with WHILE
- For optimal performance and your accepted code: Sliding Window with IF
- For an alternative technique: Prefix Sum + Binary Search

Both sliding-window approaches have O(n) time and O(1) extra
space, so both are optimal in asymptotic complexity.
"""


# ============================================================
# INTERVIEW-READY EXPLANATION
# ============================================================

"""
"I used a sliding-window approach with two pointers.

The right pointer expands the window, and I maintain the number
of zeros inside the window.

Whenever the zero count exceeds k, I move the left pointer
forward. If the element leaving the window is zero, I decrement
the zero count.

I update the maximum length only when the window contains at
most k zeros. This ensures that the answer represents the
maximum number of consecutive ones achievable with at most
k flips.

Both pointers move only forward, so the time complexity is O(n),
and the auxiliary space complexity is O(1)."


# ============================================================
# FILE NAME
# ============================================================

# LeetCode_1004_Max_Consecutive_Ones_III.py
