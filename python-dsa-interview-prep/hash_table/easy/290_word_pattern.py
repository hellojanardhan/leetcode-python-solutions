# LeetCode 290 - Word Pattern
# Difficulty: Easy
# Recommended Approach: Bidirectional HashMap
# Recommended Current-Level Approach: Bidirectional HashMap


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Two HashMaps - Bidirectional Mapping
# Your Approach
# Recommended Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# s ni words ga split cheyadaniki O(n) time padutundi.
# Tarvata pattern mariyu words ni okasari traverse chestunnam.
# Dictionary lookup/update average-ga O(1).
# Kabatti overall time complexity O(n).
#
# Space Explanation:
# pattern character -> word mapping oka dictionary lo,
# word -> pattern character reverse mapping inkoka dictionary lo
# store chestunnam.
# Maximum unique mappings k untayi.
# Kabatti auxiliary space complexity O(k).
class Solution1:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        mapping = {}
        reverse_mapping = {}

        for source, target in zip(pattern, words):

            if source in mapping and mapping[source] != target:
                return False

            if (
                target in reverse_mapping
                and reverse_mapping[target] != source
            ):
                return False

            mapping[source] = target
            reverse_mapping[target] = source

        return True


# ============================================================


# Approach 2: One HashMap + Used HashSet
# Recommended Simple Alternative
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# Words split cheyadaniki O(n).
# Pattern-word pairs ni okasari traverse chestunnam.
# HashMap mariyu HashSet operations average-ga O(1).
# Kabatti total time complexity O(n).
#
# Space Explanation:
# mapping lo source character -> target word store chestunnam.
# used_words set lo already assigned target words store chestunnam.
# Maximum k unique values untayi.
# Kabatti space complexity O(k).
class Solution2:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        mapping = {}
        used_words = set()

        for source, target in zip(pattern, words):

            if source in mapping:
                if mapping[source] != target:
                    return False

            else:
                if target in used_words:
                    return False

                mapping[source] = target
                used_words.add(target)

        return True


# ============================================================


# Approach 3: Last Seen Index Using Two HashMaps
# Very Clean Interview Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# Pattern and words ni okasari traverse chestunnam.
# Prati iteration lo previous index lookup mariyu update O(1) average.
# Kabatti total time complexity O(n).
#
# Space Explanation:
# Pattern characters last-seen indexes oka dictionary lo,
# words last-seen indexes inkoka dictionary lo store chestunnam.
# Maximum k unique entries untayi.
# Kabatti space complexity O(k).
class Solution3:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        pattern_seen = {}
        word_seen = {}

        for index, (char, word) in enumerate(zip(pattern, words)):

            if pattern_seen.get(char) != word_seen.get(word):
                return False

            pattern_seen[char] = index
            word_seen[word] = index

        return True


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Unique Pair Set Comparison
# Mathematical Hashing Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# set(pattern), set(words), set(zip(pattern, words))
# create cheyadaniki linear traversal avasaram.
# Kabatti overall time complexity O(n).
#
# Space Explanation:
# Unique characters, words, character-word pairs sets lo
# store avutayi.
# Kabatti auxiliary space complexity O(k).
class Solution4:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        return (
            len(set(pattern))
            == len(set(words))
            == len(set(zip(pattern, words)))
        )


# ============================================================


# Approach 5: Normalize Both Into First-Occurrence Patterns
# Easy to Understand but Less Efficient
# Time Complexity: O(n^2)
# Space Complexity: O(n)
#
# Time Explanation:
# pattern.index() mariyu words.index() first occurrence search chestayi.
# index() worst case lo complete sequence ni scan cheyyachu.
# Prati element kosam index() call chestunnam.
# Kabatti worst-case time complexity O(n^2).
#
# Space Explanation:
# Normalized pattern lists create chestunnam.
# Kabatti auxiliary space complexity O(n).
class Solution5:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        pattern_form = [
            pattern.index(char)
            for char in pattern
        ]

        word_form = [
            words.index(word)
            for word in words
        ]

        return pattern_form == word_form
