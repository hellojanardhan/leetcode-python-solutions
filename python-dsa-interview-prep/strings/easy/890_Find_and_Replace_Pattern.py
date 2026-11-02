
# LeetCode 890 - Find and Replace Pattern
# Difficulty: Medium
#
# Recommended Approach:
# Two Hashmaps + Bidirectional Mapping
#
# Recommended Current-Level Approach:
# Two Hashmaps + Character Mapping
#
# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Two Hashmaps + Bidirectional Mapping
# Your Approach
# Recommended Current-Level Approach
# Time Complexity: O(n * m)
# Space Complexity: O(m)
#
# Time Explanation:
# n = number of words
# m = length of each word
#
# First, words list ni traverse chestham.
#
# Word length and pattern length different ga unte,
# aa word ni skip chestham.
#
# Prati word kosam two dictionaries create chestham:
#
# word_to_pattern: word character -> pattern character
# pattern_to_word: pattern character -> word character
#
# Both mappings maintain cheyyadam valla
# one-to-one relationship enforce avuthundi.
#
# Mapping conflict unte, exists = False chestham.
#
# Word lo m characters process chestham.
# N words ki total time:
# O(n * m).
#
# Space Explanation:
# Current word kosam two dictionaries use chestham.
# Each dictionary lo at most m mappings untayi.
#
# Auxiliary space:
# O(m).
#
# Result list lo matching words store chestham.
# Result space separate ga O(n * m) varaku undachu.

class Solution1:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        result = []

        for word in words:
            if len(word) != len(pattern):
                continue

            word_to_pattern = {}
            pattern_to_word = {}
            matches = True

            for w, p in zip(word, pattern):
                if w in word_to_pattern:
                    if word_to_pattern[w] != p:
                        matches = False
                        break
                else:
                    word_to_pattern[w] = p

                if p in pattern_to_word:
                    if pattern_to_word[p] != w:
                        matches = False
                        break
                else:
                    pattern_to_word[p] = w

            if matches:
                result.append(word)

        return result


# ============================================================
# Approach 2: zip() + Two Hashmaps
# Alternative Optimal Approach
# Time Complexity: O(n * m)
# Auxiliary Space Complexity: O(m)
#
# Time Explanation:
# zip(word, pattern) corresponding characters ni pair chestundi.
#
# Prati pair ki two mapping directions validate chestham.
#
# Existing mapping conflict ayite,
# current word pattern match avvadu.
#
# Each word takes O(m) time.
# For n words:
# O(n * m).
#
# Space Explanation:
# Two dictionaries lo current word mappings store chestham.
#
# Auxiliary space:
# O(m).
#
# Result list space separate ga O(n * m) varaku undachu.

class Solution2:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        result = []

        for word in words:
            if len(word) != len(pattern):
                continue

            mapping1 = {}
            mapping2 = {}
            matches = True

            for char_word, char_pattern in zip(word, pattern):
                if (
                    char_word in mapping1
                    and mapping1[char_word] != char_pattern
                ):
                    matches = False
                    break

                if (
                    char_pattern in mapping2
                    and mapping2[char_pattern] != char_word
                ):
                    matches = False
                    break

                mapping1[char_word] = char_pattern
                mapping2[char_pattern] = char_word

            if matches:
                result.append(word)

        return result


# ============================================================
# Approach 3: Pattern Signature
# Alternative Optimal Approach
# Time Complexity: O(n * m)
# Auxiliary Space Complexity: O(m)
#
# Time Explanation:
# Each word and the pattern ni canonical signature ga convert chestham.
#
# Example:
# "mee" -> (0, 1, 1)
# "aqq" -> (0, 1, 1)
# "abc" -> (0, 1, 2)
#
# First occurrence ki new number assign chestham.
# Repeated character ki previous number reuse chestham.
#
# Word signature and pattern signature equal ayite,
# word pattern match avuthundi.
#
# Each signature calculation O(m).
# For n words:
# O(n * m).
#
# Space Explanation:
# Signature generation kosam dictionary and signature list use chestham.
#
# Auxiliary space:
# O(m).
#
# Result list space separate ga O(n * m) varaku undachu.

class Solution3:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:

        def signature(text: str) -> tuple:
            seen = {}
            result = []

            for char in text:
                if char not in seen:
                    seen[char] = len(seen)

                result.append(seen[char])

            return tuple(result)

        pattern_signature = signature(pattern)
        result = []

        for word in words:
            if len(word) != len(pattern):
                continue

            if signature(word) == pattern_signature:
                result.append(word)

        return result


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================
#
# The three approaches above are optimal in asymptotic time.
#
# Approach 1 is recommended for your current level because
# it directly applies the two-dictionary technique you learned
# in Word Pattern and Isomorphic Strings.
#
# Approach 3 is useful when you want to compare character
# repetition patterns using a canonical representation.


# ============================================================
# DRY RUN
# ============================================================
#
# Input:
# words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
# pattern = "abb"
#
# Pattern mapping structure:
# Position 0 -> unique character
# Position 1 -> repeated character
# Position 2 -> same character as position 1
#
# Word: "abc"
# a -> a
# b -> b
# c -> b
# But b already maps to pattern character b.
# c cannot also map to b.
# Result: No match
#
# Word: "deq"
# d -> a
# e -> b
# q -> b
# e and q would map to the same pattern character.
# Result: No match
#
# Word: "mee"
# m -> a
# e -> b
# e -> b
# Both mappings are consistent.
# Result: Match
#
# Word: "aqq"
# a -> a
# q -> b
# q -> b
# Both mappings are consistent.
# Result: Match
#
# Word: "dkd"
# d appears at positions 0 and 2.
# Pattern character a at position 0 differs from b at position 2.
# Result: No match
#
# Word: "ccc"
# Same character would need to map to a and b.
# Result: No match
#
# Output:
# ["mee", "aqq"]


# ============================================================
# IMPORTANT TEST CASES
# ============================================================
#
# words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
# pattern = "abb"
# Output: ["mee", "aqq"]
#
# words = ["abc", "def", "ghi"]
# pattern = "abc"
# Output: ["abc", "def", "ghi"]
#
# words = ["aaa", "bbb", "abc"]
# pattern = "aaa"
# Output: ["aaa", "bbb"]
#
# words = ["a", "bb", "c"]
# pattern = "a"
# Output: ["a", "c"]
#
# words = ["ab", "aa", "bc"]
# pattern = "ab"
# Output: ["ab", "bc"]


# ============================================================
# INTERVIEW-READY EXPLANATION
# ============================================================
#
# I iterate through each word and skip words whose length differs
# from the pattern length.
#
# For every remaining word, I use two hashmaps to enforce
# a one-to-one character mapping between the word and the pattern.
#
# If either mapping conflicts, the word is rejected.
# If all character pairs are consistent, the word is added
# to the result.
#
# Time Complexity: O(n * m), where n is the number of words
# and m is the pattern length.
#
# Auxiliary Space Complexity: O(m) for the two mappings
# used to process one word.
#
# The result list can use up to O(n * m) additional space.
