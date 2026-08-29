# LeetCode 1941 - Check if All Characters Have Equal Number of Occurrences
# Difficulty: Easy
# Recommended Approach: Frequency HashMap + all()
# Recommended Current-Level Approach: Frequency HashMap + all()


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Frequency HashMap + all()
# Your Approach
# Recommended Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# String lo prati character frequency ni calculate cheyadaniki O(n).
# k frequency values ni first frequency tho compare cheyadaniki O(k).
# O(n + k), simplified-ga total time complexity O(n).
#
# Space Explanation:
# k unique characters frequencies dictionary lo store avutayi.
# Kabatti auxiliary space complexity O(k).
# Lowercase English letters maatrame kabatti maximum 26 entries untayi.
class Solution1:
    def areOccurrencesEqual(self, s: str) -> bool:
        frequency = {}

        for char in s:
            frequency[char] = frequency.get(char, 0) + 1

        first_count = next(iter(frequency.values()))

        return all(
            first_count == count
            for count in frequency.values()
        )


# ============================================================


# Approach 2: Frequency HashMap + Set
# Short Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# Character frequencies calculate cheyadaniki O(n).
# Frequency values ni set ga convert cheyadaniki O(k).
# Set length check O(1).
# Kabatti total time complexity O(n).
#
# Space Explanation:
# Frequency dictionary mariyu frequency set use chestunnam.
# Rendu structures lo maximum k values untayi.
# Kabatti auxiliary space complexity O(k).
class Solution2:
    def areOccurrencesEqual(self, s: str) -> bool:
        frequency = {}

        for char in s:
            frequency[char] = frequency.get(char, 0) + 1

        return len(set(frequency.values())) == 1


# ============================================================


# Approach 3: Fixed-Size Frequency Array
# Recommended Optimal Space Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Time Explanation:
# String lo prati character frequency ni fixed array lo update chestunnam.
# Fixed 26 frequencies ni equality kosam check chestunnam.
# O(n + 26), simplified-ga total time complexity O(n).
#
# Space Explanation:
# Fixed size 26 array maatrame use chestunnam.
# Input size periginaa array size maaradu.
# Kabatti auxiliary space complexity O(1).
class Solution3:
    def areOccurrencesEqual(self, s: str) -> bool:
        frequency = [0] * 26

        for char in s:
            index = ord(char) - ord("a")
            frequency[index] += 1

        expected_count = 0

        for count in frequency:
            if count > 0:
                expected_count = count
                break

        for count in frequency:
            if count > 0 and count != expected_count:
                return False

        return True


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: collections.Counter + Set
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# Counter character frequencies ni O(n) time lo calculate chestundi.
# Frequency values ni set ga convert cheyadaniki O(k).
# Kabatti total time complexity O(n).
#
# Space Explanation:
# Counter mariyu frequency set lo maximum k entries untayi.
# Kabatti auxiliary space complexity O(k).
class Solution4:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter

        frequency = Counter(s)

        return len(set(frequency.values())) == 1


# ============================================================


# Approach 5: Count Every Unique Character
# Time Complexity: O(k * n)
# Space Complexity: O(k)
#
# Time Explanation:
# String lo k unique characters unnayi.
# Prati unique character kosam s.count() complete string ni scan chestundi.
# Kabatti total time complexity O(k * n).
# Worst case lo k nearly n ayite O(n^2).
#
# Space Explanation:
# Unique characters ni set lo store chestunnam.
# Kabatti auxiliary space complexity O(k).
class Solution5:
    def areOccurrencesEqual(self, s: str) -> bool:
        unique_characters = set(s)
        first_character = next(iter(unique_characters))
        expected_count = s.count(first_character)

        for char in unique_characters:
            if s.count(char) != expected_count:
                return False

        return True
