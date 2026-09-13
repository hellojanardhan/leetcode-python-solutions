# LeetCode 567 - Permutation in String
# Difficulty: Medium

# Recommended Approach: Fixed Sliding Window + Frequency Array
# Recommended Current-Level Approach: Fixed Sliding Window + HashMap


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Rebuild Frequency HashMap for Every Window
# Your Approach
# Correct Approach
# Time Complexity: O((n-k+1) * k)
# Space Complexity: O(k)
#
# Time Explanation:
# k = len(s1)
# n = len(s2)
#
# s2 lo total possible k-size windows:
# n-k+1
#
# Prati window lo:
#
# s2[i:j] slice create chestunnam -> O(k)
#
# Tarvata aa k characters ni loop chesi
# current_freq create chestunnam -> O(k)
#
# Dictionary comparison k unique characters varaku check cheyyachu -> O(k)
#
# So one window:
#
# O(k) + O(k) + O(k)
# = O(k)
#
# Total:
#
# O((n-k+1) * k)
#
# Worst-case simplify cheste:
# O(n * k)
#
# Space Explanation:
# freq -> maximum k characters
# current_freq -> maximum k characters
# string -> k-size substring
#
# Same time lo O(k) extra memory use avutundi.
class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}

        for char in s1:
            freq[char] = freq.get(char, 0) + 1

        k = len(s1)
        i = 0
        j = k
        n = len(s2)

        while j <= n:
            current_freq = {}

            string = s2[i:j]

            for char in string:
                current_freq[char] = current_freq.get(char, 0) + 1

            if freq == current_freq:
                return True

            i += 1
            j += 1

        return False


# ============================================================


# Approach 2: Fixed Sliding Window + HashMap
# Recommended Current-Level Optimized Approach
# Time Complexity: O(n)
# Space Complexity: O(1) for lowercase English alphabet
#
# Time Explanation:
# First s1 frequency map create chestunnam.
#
# First k-size s2 window frequency map kuda create chestunnam.
#
# Tarvata window move ayye prati sari:
#
# outgoing character frequency -= 1
# incoming character frequency += 1
#
# Window motham malli scan cheyyatledu.
#
# English lowercase letters only 26 kabatti
# dictionary comparison maximum 26 keys varake untundi.
#
# 26 constant kabatti:
#
# O(26 * n) = O(n)
#
# Space Explanation:
# Maximum 26 lowercase letters maatrame frequency maps lo untayi.
#
# O(26) = O(1).
class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        k = len(s1)

        freq = {}
        current_freq = {}

        for char in s1:
            freq[char] = freq.get(char, 0) + 1

        for i in range(k):
            char = s2[i]
            current_freq[char] = current_freq.get(char, 0) + 1

        if freq == current_freq:
            return True

        for right in range(k, len(s2)):
            outgoing = s2[right - k]
            incoming = s2[right]

            current_freq[outgoing] -= 1

            if current_freq[outgoing] == 0:
                del current_freq[outgoing]

            current_freq[incoming] = current_freq.get(incoming, 0) + 1

            if freq == current_freq:
                return True

        return False


# ============================================================


# Approach 3: Fixed Sliding Window + Frequency Array
# Recommended Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Time Explanation:
# English lowercase alphabet size 26.
#
# s1 kosam one 26-size array.
# current window kosam one 26-size array.
#
# Window move ayye prati sari:
#
# outgoing frequency -= 1
# incoming frequency += 1
#
# Arrays compare cheyyadaniki 26 positions maatrame.
#
# 26 constant kabatti:
#
# O(26 * n)
# = O(n)
#
# Space Explanation:
# Two arrays of exactly 26 elements.
#
# O(26 + 26)
# = O(1).
class Solution3:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        k = len(s1)

        freq1 = [0] * 26
        freq2 = [0] * 26

        for i in range(k):
            freq1[ord(s1[i]) - ord("a")] += 1
            freq2[ord(s2[i]) - ord("a")] += 1

        if freq1 == freq2:
            return True

        for right in range(k, len(s2)):
            incoming = ord(s2[right]) - ord("a")
            outgoing = ord(s2[right - k]) - ord("a")

            freq2[outgoing] -= 1
            freq2[incoming] += 1

            if freq1 == freq2:
                return True

        return False


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Sort Every Window
# Time Complexity: O((n-k+1) * k log k)
# Space Complexity: O(k)
#
# s1 ni sort chestham.
# Prati k-size substring ni sort chesi compare chestham.
#
# Correct but inefficient.
class Solution4:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        if k > len(s2):
            return False

        target = sorted(s1)

        for i in range(len(s2) - k + 1):
            if sorted(s2[i:i + k]) == target:
                return True

        return False
