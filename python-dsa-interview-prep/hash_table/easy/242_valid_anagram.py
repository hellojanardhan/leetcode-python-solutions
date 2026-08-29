# LeetCode 242 - Valid Anagram
# Difficulty: Easy
# Recommended Approach: One Frequency HashMap
# Recommended Current-Level Approach: Two Frequency HashMaps


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Two Frequency HashMaps
# Your Approach
# Recommended Current-Level Approach
# Time Complexity: O(n + m)
# Space Complexity: O(k)
#
# Time Explanation:
# s lo prati character ni okasari traverse chestunnam.
# t lo prati character ni okasari traverse chestunnam.
# Dictionary get mariyu update average-ga O(1).
# Kabatti total time complexity O(n + m).
#
# Space Explanation:
# Rendu strings character frequencies ni dictionaries lo store chestunnam.
# k unique characters unte auxiliary space complexity O(k).
# Lowercase English letters maatrame unte maximum 26 entries untayi.
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        s_frequency = {}
        t_frequency = {}

        for char in s:
            s_frequency[char] = s_frequency.get(char, 0) + 1

        for char in t:
            t_frequency[char] = t_frequency.get(char, 0) + 1

        return s_frequency == t_frequency


# ============================================================


# Approach 2: One Frequency HashMap
# Recommended HashMap Approach
# Time Complexity: O(n + m)
# Space Complexity: O(k)
#
# Time Explanation:
# s characters frequencies ni dictionary lo increase chestunnam.
# t characters vachinappudu frequencies ni decrease chestunnam.
# Rendu strings ni okkokkasaari traverse chestunnam.
# Kabatti total time complexity O(n + m).
#
# Space Explanation:
# Oka frequency dictionary maatrame create chestunnam.
# k unique characters unte auxiliary space complexity O(k).
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency = {}

        for char in s:
            frequency[char] = frequency.get(char, 0) + 1

        for char in t:
            if char not in frequency:
                return False

            frequency[char] -= 1

            if frequency[char] < 0:
                return False

        return True


# ============================================================


# Approach 3: Fixed-Size Frequency Array
# Recommended Optimal Space Approach
# Time Complexity: O(n + m)
# Space Complexity: O(1)
#
# Time Explanation:
# s characters kosam corresponding frequency increase chestunnam.
# t characters kosam corresponding frequency decrease chestunnam.
# Rendu strings ni okkokkasaari process chestunnam.
# Kabatti total time complexity O(n + m).
#
# Space Explanation:
# Fixed size 26 array maatrame use chestunnam.
# Input size periginaa array size maaradu.
# Kabatti auxiliary space complexity O(1).
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency = [0] * 26

        for char in s:
            index = ord(char) - ord("a")
            frequency[index] += 1

        for char in t:
            index = ord(char) - ord("a")
            frequency[index] -= 1

            if frequency[index] < 0:
                return False

        return True


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: collections.Counter
# Time Complexity: O(n + m)
# Space Complexity: O(k)
#
# Time Explanation:
# Counter s mariyu t character frequencies ni calculate chestundi.
# Rendu strings total-ga process avutayi.
# Kabatti total time complexity O(n + m).
#
# Space Explanation:
# Rendu Counter objects unique character frequencies ni store chestayi.
# k unique characters unte auxiliary space complexity O(k).
class Solution4:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        return Counter(s) == Counter(t)


# ============================================================


# Approach 5: Sorting
# Time Complexity: O(n log n + m log m)
# Space Complexity: O(n + m)
#
# Time Explanation:
# s ni sort cheyadaniki O(n log n) time padutundi.
# t ni sort cheyadaniki O(m log m) time padutundi.
# Sorted results compare cheyadaniki O(n + m) time padavachu.
# Kabatti total time O(n log n + m log m).
#
# Space Explanation:
# Python sorted() kotta character lists create chestundi.
# Kabatti auxiliary space complexity O(n + m).
class Solution5:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


# ============================================================


# Approach 6: Count Every Character
# Time Complexity: O(k * (n + m))
# Space Complexity: O(k)
#
# Time Explanation:
# Prati unique character kosam s.count() mariyu t.count() call chestunnam.
# count() complete string ni scan chestundi.
# k unique characters unte total time O(k * (n + m)).
#
# Space Explanation:
# Unique characters ni set lo store chestunnam.
# Kabatti auxiliary space complexity O(k).
class Solution6:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        unique_characters = set(s)

        for char in unique_characters:
            if s.count(char) != t.count(char):
                return False

        return True
