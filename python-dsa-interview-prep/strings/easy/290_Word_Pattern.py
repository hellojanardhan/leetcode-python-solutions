
# LeetCode 290 - Word Pattern
# Difficulty: Easy
#
# Recommended Approach:
# Two Hashmaps
#
# Recommended Current-Level Approach:
# Two Hashmaps + Bidirectional Mapping
#
# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Two Hashmaps + Bidirectional Mapping
# Your Approach
# Recommended Current-Level Approach
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
#
# Time Explanation:
# First, input string ni words ga split chestham.
#
# Pattern length and words count equal ga unnayo check chestham.
# Equal kakapothe False return chestham.
#
# Tarvata two dictionaries maintain chestham:
# char_to_word: pattern character -> word
# word_to_char: word -> pattern character
#
# Prati character-word pair ni check chestham.
#
# Character already dictionary lo unte,
# mapped word same undali.
# Different word ayite False return chestham.
#
# Word already dictionary lo unte,
# mapped character same undali.
# Different character ayite False return chestham.
#
# String splitting O(m).
# Pattern traversal O(n).
# Dictionary lookups and updates average O(1).
#
# Total time complexity:
# O(n + m).
#
# Space Explanation:
# Words list lo words store chestham.
# Two dictionaries lo mappings store chestham.
#
# Worst case lo words and mappings input size ki proportional ga
# grow avuthayi.
#
# Auxiliary space:
# O(n + m).

class Solution1:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        char_to_word = {}
        word_to_char = {}

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word

            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char

        return True


# ============================================================
# Approach 2: zip() + Two Hashmaps
# Alternative Optimal Approach
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
#
# Time Explanation:
# First, string ni words ga split chestham.
#
# Pattern length and words count equal kakapothe,
# False return chestham.
#
# zip(pattern, words) character and word ni pair chestundi.
#
# Prati pair ki both mappings validate chestham:
# character -> word
# word -> character
#
# Mapping conflict unte False return chestham.
#
# Total time complexity:
# O(n + m).
#
# Space Explanation:
# Words list and two dictionaries use chestham.
#
# Auxiliary space:
# O(n + m).

class Solution2:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if char in char_to_word and char_to_word[char] != word:
                return False

            if word in word_to_char and word_to_char[word] != char:
                return False

            char_to_word[char] = word
            word_to_char[word] = char

        return True


# ============================================================
# Approach 3: Set + zip() Uniqueness Check
# Concise Optimal Approach
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
#
# Time Explanation:
# First, words ni split chestham.
#
# Pattern length and words count equal undali.
#
# Tarvata three unique counts compare chestham:
#
# 1. Unique pattern characters
# 2. Unique words
# 3. Unique character-word pairs
#
# Ee three counts equal ayite,
# mapping one-to-one ga undi ani confirm cheyochu.
#
# Total time complexity:
# O(n + m).
#
# Space Explanation:
# Sets lo unique characters, words and pairs store chestham.
#
# Auxiliary space:
# O(n + m).
#
# Note:
# Idi concise approach.
# Interview lo Approach 1 explain cheyadam usually easier.

class Solution3:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        return (
            len(set(pattern))
            == len(set(words))
            == len(set(zip(pattern, words)))
        )


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================
#
# Approach 1 and Approach 2 are the clearest choices for interviews.
# Approach 3 is a compact alternative.
#
# No need to add redundant approaches just to increase the count.


# ============================================================
# DRY RUN
# ============================================================
#
# Input:
# pattern = "abba"
# s = "dog cat cat dog"
#
# words = ["dog", "cat", "cat", "dog"]
#
# Initial dictionaries:
# char_to_word = {}
# word_to_char = {}
#
# Index 0:
# char = "a"
# word = "dog"
# Store a -> dog and dog -> a
#
# Index 1:
# char = "b"
# word = "cat"
# Store b -> cat and cat -> b
#
# Index 2:
# char = "b"
# word = "cat"
# Existing mappings match.
#
# Index 3:
# char = "a"
# word = "dog"
# Existing mappings match.
#
# All pairs are valid.
# Output: True
#
#
# Example 2:
# pattern = "abba"
# s = "dog cat cat fish"
#
# At index 3:
# char = "a"
# word = "fish"
#
# But "a" is already mapped to "dog".
# Mapping conflict occurs.
#
# Output: False


# ============================================================
# IMPORTANT TEST CASES
# ============================================================

# ("abba", "dog cat cat dog")   -> True
# ("abba", "dog cat cat fish")  -> False
# ("aaaa", "dog dog dog dog")   -> True
# ("abba", "dog dog dog dog")   -> False
# ("abc", "one two three")      -> True
# ("abc", "one two")            -> False
# ("", "")                      -> True


# ============================================================
# INTERVIEW-READY EXPLANATION
# ============================================================
#
# I split the input string into words and check whether the
# number of words equals the pattern length.
#
# I use two hashmaps to maintain a one-to-one relationship:
# one maps each pattern character to a word, and the other maps
# each word back to a character.
#
# If either mapping conflicts with an existing mapping,
# I return False. If all pairs are consistent, I return True.
#
# Time Complexity: O(n + m), including splitting the string.
# Auxiliary Space Complexity: O(n + m), for the words list
# and the two hashmaps.
