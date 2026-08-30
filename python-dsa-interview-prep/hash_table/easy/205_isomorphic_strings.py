# LeetCode 205 - Isomorphic Strings
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
# s mariyu t characters ni zip() tho okasari traverse chestunnam.
# Prati character pair kosam dictionary lookup/update average-ga O(1).
# Kabatti total time complexity O(n).
#
# Space Explanation:
# source -> target mappings oka dictionary lo,
# target -> source mappings reverse dictionary lo store chestunnam.
# Maximum k unique characters mappings untayi.
# Kabatti auxiliary space complexity O(k).
class Solution1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        reverse_mapping = {}

        for source, target in zip(s, t):

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
# Prati source-target character pair ni okasari process chestunnam.
# HashMap mariyu HashSet lookup average-ga O(1).
# Kabatti total time complexity O(n).
#
# Space Explanation:
# mapping dictionary lo source -> target store chestunnam.
# used_targets set lo already assigned target characters store chestunnam.
# Maximum k unique values untayi.
# Kabatti auxiliary space complexity O(k).
class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        used_targets = set()

        for source, target in zip(s, t):

            if source in mapping:
                if mapping[source] != target:
                    return False

            else:
                if target in used_targets:
                    return False

                mapping[source] = target
                used_targets.add(target)

        return True


# ============================================================


# Approach 3: Last Seen Index Using Two HashMaps
# Clean Pattern-Matching Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# Strings ni okasari traverse chestunnam.
# Prati character ki last-seen index lookup/update average-ga O(1).
# Kabatti total time complexity O(n).
#
# Space Explanation:
# s characters last-seen positions oka dictionary lo,
# t characters last-seen positions inkoka dictionary lo store chestunnam.
# Kabatti auxiliary space complexity O(k).
class Solution3:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_seen = {}
        t_seen = {}

        for index, (source, target) in enumerate(zip(s, t)):

            if s_seen.get(source) != t_seen.get(target):
                return False

            s_seen[source] = index
            t_seen[target] = index

        return True


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Compare Unique Mapping Pairs
# Mathematical HashSet Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
#
# Time Explanation:
# set(s), set(t), mariyu set(zip(s, t))
# create cheyadaniki strings ni linear-ga process chestundi.
# Kabatti total time complexity O(n).
#
# Space Explanation:
# Unique characters mariyu character pairs sets lo store avutayi.
# Kabatti auxiliary space complexity O(k).
class Solution4:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return (
            len(set(s))
            == len(set(t))
            == len(set(zip(s, t)))
        )


# ============================================================


# Approach 5: First Occurrence Pattern Using index()
# Simple but Less Efficient
# Time Complexity: O(n^2)
# Space Complexity: O(n)
#
# Time Explanation:
# index() first occurrence kosam string ni scan chestundi.
# Prati character kosam index() repeatedly call chestunnam.
# Worst case lo O(n) work ni n times chestundi.
# Kabatti time complexity O(n^2).
#
# Space Explanation:
# s_pattern mariyu t_pattern lists create chestunnam.
# Kabatti auxiliary space complexity O(n).
class Solution5:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_pattern = [s.index(char) for char in s]
        t_pattern = [t.index(char) for char in t]

        return s_pattern == t_pattern
