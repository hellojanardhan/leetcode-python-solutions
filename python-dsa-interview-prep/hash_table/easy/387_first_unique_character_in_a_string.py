# LeetCode 387 - First Unique Character in a String
# Difficulty: Easy
# Recommended Approach: Frequency HashMap + Second Pass
# Recommended Current-Level Approach: Frequency HashMap + Second Pass


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Frequency HashMap + Second Pass
# Your Approach
# Recommended HashMap Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# First loop lo string characters frequencies calculate chestunnam.
# Second loop lo original string ni malli okasari traverse chestunnam.
# Dictionary lookup mariyu update average-ga O(1).
# O(n) + O(n) = O(2n), simplified-ga O(n).
#
# Space Explanation:
# k unique characters frequencies ni dictionary lo store chestunnam.
# Kabatti auxiliary space complexity O(k).
# Lowercase English letters maatrame unte maximum 26 entries kabatti O(1).
class Solution1:
    def firstUniqChar(self, s: str) -> int:
        frequency = {}

        for char in s:
            frequency[char] = frequency.get(char, 0) + 1

        for index, char in enumerate(s):
            if frequency[char] == 1:
                return index

        return -1


# ============================================================


# Approach 2: Fixed-Size Frequency Array
# Recommended Optimal Space Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Time Explanation:
# First pass lo characters frequencies fixed array lo calculate chestunnam.
# Second pass lo first frequency 1 character index find chestunnam.
# Rendu passes kalipi total time complexity O(n).
#
# Space Explanation:
# Fixed size 26 integer array maatrame use chestunnam.
# Input size periginaa array size maaradu.
# Kabatti auxiliary space complexity O(1).
class Solution2:
    def firstUniqChar(self, s: str) -> int:
        frequency = [0] * 26

        for char in s:
            index = ord(char) - ord("a")
            frequency[index] += 1

        for index, char in enumerate(s):
            char_index = ord(char) - ord("a")

            if frequency[char_index] == 1:
                return index

        return -1


# ============================================================


# Approach 3: collections.Counter
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# Counter string characters frequencies ni O(n) time lo calculate chestundi.
# Tarvata string ni okasari traverse chesi first unique index find chestunnam.
# Kabatti total time complexity O(n).
#
# Space Explanation:
# Counter lo k unique character frequencies store avutayi.
# Kabatti auxiliary space complexity O(k).
class Solution3:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter

        frequency = Counter(s)

        for index, char in enumerate(s):
            if frequency[char] == 1:
                return index

        return -1


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: find() + rfind()
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Time Explanation:
# Fixed 26 lowercase letters maatrame traverse chestunnam.
# Prati character kosam find() mariyu rfind() string ni scan chestayi.
# O(26 * 2n) = O(52n), constants remove cheste O(n).
#
# Space Explanation:
# Konni variables mariyu fixed alphabet string maatrame use chestunnam.
# Kabatti auxiliary space complexity O(1).
class Solution4:
    def firstUniqChar(self, s: str) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        first_index = len(s)

        for char in alphabet:
            left = s.find(char)

            if left != -1 and left == s.rfind(char):
                first_index = min(first_index, left)

        if first_index == len(s):
            return -1

        return first_index


# ============================================================


# Approach 5: count() for Every Character
# Time Complexity: O(n^2)
# Space Complexity: O(1)
#
# Time Explanation:
# String lo prati character ni traverse chestunnam.
# Prati character kosam count() complete string ni scan chestundi.
# Kabatti worst-case time complexity O(n^2).
#
# Space Explanation:
# Additional dictionary, set ledaa array create cheyadam ledu.
# Konni variables maatrame use chestunnam.
# Kabatti auxiliary space complexity O(1).
class Solution5:
    def firstUniqChar(self, s: str) -> int:
        for index, char in enumerate(s):
            if s.count(char) == 1:
                return index

        return -1
