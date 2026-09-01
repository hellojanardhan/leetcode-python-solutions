# LeetCode 49 - Group Anagrams
# Difficulty: Medium

# Recommended Approach: Character Frequency Tuple + HashMap
# Recommended Current-Level Approach: Sorted String + HashMap

# n = number of words
# k = maximum word length
# g = number of anagram groups
#
# Space convention:
# Input strings ni exclude chestunnam.
# Output list references and additional working storage include chestunnam.
# Group lists original words ki references store chestayi;
# word contents ni copy cheyavu.


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Sorted String + HashMap
# Your Approach
# Recommended Current-Level Approach
# Time Complexity: O(n * k log k)
# Space Complexity: O(n + g*k), worst case O(n*k)
#
# Time Explanation:
# Prati word ni sort cheyadaniki O(k log k).
# Sorted characters ni join cheyadaniki O(k).
# n words kosam total time O(n * k log k).
#
# Space Explanation:
# g sorted-string keys kosam O(g*k).
# Group lists lo n original-word references kosam O(n).
# Temporary sorting storage O(k).
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())


# ============================================================


# Approach 2: Character Frequency Tuple + HashMap
# Recommended Optimal Approach for Lowercase English Letters
# Time Complexity: O(n * (k + 26))
# Usually simplified to O(n*k)
# Space Complexity: O(n + 26*g), simplified to O(n)
#
# Time Explanation:
# Prati word characters ni traverse chesi frequencies calculate chestunnam.
# Fixed 26 counts ni tuple ga convert chestunnam.
# Tuple hashing kuda fixed 26 entries meeda jarugutundi.
# Sorting avasaram ledu.
#
# Space Explanation:
# Prati group key fixed 26-number tuple.
# Output groups lo n original-word references untayi.
# Kabatti total additional space O(n + 26*g) = O(n).
#
# Logic:
# Anagrams lo prati letter frequency same untundi.
# List dictionary key ga use cheyalemu.
# Kabatti frequency list ni tuple ga convert chestunnam.
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            frequency = [0] * 26

            for character in word:
                index = ord(character) - ord("a")
                frequency[index] += 1

            key = tuple(frequency)

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())


# ============================================================


# Approach 3: Counter + frozenset Signature
# Frequency-Based Alternative
# Time Complexity: O(n*k)
# Space Complexity: O(n + g*u)
#
# u = maximum distinct characters in a word.
# Lowercase English letters kabatti u <= 26.
# Ee constraints prakaram space O(n).
#
# Time Explanation:
# Counter prati word character frequencies calculate chestundi.
# frozenset character-count pairs ni order-independent key ga chestundi.
# Dictionary and set operations average-case assumptions tho O(n*k).
#
# Space Explanation:
# Prati group key lo maximum u character-count pairs untayi.
# Group lists lo total n word references untayi.
#
# Important:
# frozenset immutable and hashable kabatti dictionary key ga use cheyavachu.
class Solution3:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter

        groups = {}

        for word in strs:
            key = frozenset(Counter(word).items())

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())


# ============================================================
# OTHER USEFUL SOLUTIONS / VARIANTS
# ============================================================


# Approach 4: Sorted String + defaultdict
# Shorter Version of Approach 1
# Time Complexity: O(n * k log k)
# Space Complexity: O(n + g*k), worst case O(n*k)
#
# Time Explanation:
# Sorting and grouping logic Approach 1 tho same.
# defaultdict missing key kosam empty list automatically create chestundi.
#
# Space Explanation:
# Sorted-string keys and grouped word references store chestunnam.
#
# Note:
# Idi kotta algorithm kaadu.
# Approach 1 ki shorter implementation.
class Solution4:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        groups = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)

        return list(groups.values())


# ============================================================


# Approach 5: Compare Against Existing Groups
# Brute Force Approach
# Time Complexity: O(n^2 * k log k)
# Space Complexity: O(n + k)
#
# Time Explanation:
# Prati word kosam existing groups ni check chestunnam.
# Prati comparison lo rendu words ni sort chestunnam.
# Worst case lo O(n^2) comparisons jaragavachu.
#
# Space Explanation:
# Output groups lo n word references store chestunnam.
# Temporary sorted-character lists kosam O(k).
#
# Logic:
# Existing group first word tho anagram ayite aa group lo append chestam.
# Ye group tho match kakapothe kotta group create chestam.
class Solution5:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []

        for word in strs:
            for group in groups:
                if sorted(word) == sorted(group[0]):
                    group.append(word)
                    break
            else:
                groups.append([word])

        return groups
