
# LeetCode 205 - Isomorphic Strings
# Difficulty: Easy
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
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# First, rendu strings lengths equal ga unnayo check chestham.
#
# Equal kakapothe, False return chestham.
#
# Tarvata two dictionaries maintain chestham:
#
# s_to_t: s string character -> t string character
# t_to_s: t string character -> s string character
#
# Prati index lo corresponding characters ni compare chestham.
#
# Character already mapping lo unte,
# existing mapping same undali.
#
# Different mapping unte, False return chestham.
#
# Mapping lekapothe, dictionary lo store chestham.
#
# String ni once traverse chestunnam.
# Average dictionary lookup and update O(1).
#
# Total time complexity:
# O(n).
#
# Space Explanation:
# Unique characters and their mappings ni two dictionaries lo
# store chestham.
#
# k = maximum distinct characters stored in either mapping.
#
# Auxiliary space:
# O(k).

class Solution1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t

            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s

        return True


# ============================================================


# Approach 2: zip() + Two Hashmaps
# Alternative Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# zip(s, t) corresponding characters ni pair chestundi.
#
# Example:
# s = "egg"
# t = "add"
#
# Pairs:
# ('e', 'a')
# ('g', 'd')
# ('g', 'd')
#
# Prati pair ki both mapping directions validate chestham.
#
# Mapping conflict unte False return chestham.
#
# Total time complexity:
# O(n).
#
# Space Explanation:
# Two dictionaries lo character mappings store chestham.
#
# Auxiliary space:
# O(k).

class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            if char_s in s_to_t and s_to_t[char_s] != char_t:
                return False

            if char_t in t_to_s and t_to_s[char_t] != char_s:
                return False

            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True


# ============================================================


# Approach 3: Last-Seen Index Mapping
# Alternative Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# Prati character last time ye index lo kanipinchindo
# dictionaries lo store chestham.
#
# Two dictionaries maintain chestham:
# last_s: characters in s -> last seen index
# last_t: characters in t -> last seen index
#
# Current characters last-seen indices equal ga unte,
# their previous occurrence patterns match avuthayi.
#
# Indices different ga unte, mapping pattern different.
# Appudu False return chestham.
#
# Tarvata current index ni both dictionaries lo update chestham.
#
# String ni once traverse chestham.
#
# Total time complexity:
# O(n).
#
# Space Explanation:
# Distinct characters last-seen indices ni store chestham.
#
# Auxiliary space:
# O(k).
#
# Note:
# This approach is concise, but Approach 1 is often easier
# to explain when first learning bidirectional mapping.

class Solution3:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        last_s = {}
        last_t = {}

        for i, (char_s, char_t) in enumerate(zip(s, t)):
            if last_s.get(char_s, -1) != last_t.get(char_t, -1):
                return False

            last_s[char_s] = i
            last_t[char_t] = i

        return True


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================
#
# The three approaches above are all O(n) time solutions.
#
# Approach 1 is the clearest for interviews because it explicitly
# checks both mapping directions.
#
# No need to add redundant approaches just to increase the count.


# ============================================================
# DRY RUN - TRUE CASE
# ============================================================
#
# Input:
# s = "egg"
# t = "add"
#
# Initially:
# s_to_t = {}
# t_to_s = {}
#
# Index 0:
# char_s = 'e'
# char_t = 'a'
#
# Store:
# e -> a
# a -> e
#
# Index 1:
# char_s = 'g'
# char_t = 'd'
#
# Store:
# g -> d
# d -> g
#
# Index 2:
# char_s = 'g'
# char_t = 'd'
#
# Both existing mappings match.
#
# No conflict found.
# Output: True


# ============================================================
# DRY RUN - FALSE CASE
# ============================================================
#
# Input:
# s = "foo"
# t = "bar"
#
# Index 0:
# f -> b
# b -> f
#
# Index 1:
# o -> a
# a -> o
#
# Index 2:
# s character = 'o'
# t character = 'r'
#
# But 'o' is already mapped to 'a'.
# Current character 'o' is paired with 'r'.
#
# Mapping conflict occurs.
# Output: False


# ============================================================
# IMPORTANT TEST CASES
# ============================================================
#
# ("egg", "add")       -> True
# ("foo", "bar")       -> False
# ("paper", "title")   -> True
# ("ab", "aa")         -> False
# ("a", "a")           -> True
# ("ab", "ca")         -> True
# ("", "")             -> True
# ("abc", "de")        -> False


# ============================================================
# INTERVIEW-READY EXPLANATION
# ============================================================
#
# First, I check whether both strings have equal lengths.
#
# Then I use two hashmaps to maintain a one-to-one mapping
# between characters in the two strings.
#
# One hashmap maps characters from s to characters in t.
# The other hashmap maps characters from t back to s.
#
# If either mapping conflicts with an existing mapping,
# I return False. Otherwise, after processing all characters,
# I return True.
#
# Time Complexity: O(n).
# Auxiliary Space Complexity: O(k), where k is the number
# of distinct characters stored in the mappings.
