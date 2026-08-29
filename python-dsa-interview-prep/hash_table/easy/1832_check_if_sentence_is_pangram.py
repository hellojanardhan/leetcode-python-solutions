# LeetCode 1832 - Check if the Sentence Is Pangram
# Difficulty: Easy
# Recommended Approach: HashSet with Early Return
# Recommended Current-Level Approach: HashSet


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: HashSet
# Your Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Time Explanation:
# Sentence lo unna prati character ni okasari traverse chestunnam.
# Set lookup mariyu insertion average-ga O(1) untayi.
# Kabatti total time complexity O(n).
#
# Space Explanation:
# Sentence lo lowercase English letters maatrame untayi.
# Set lo maximum 26 characters maatrame store avutayi.
# 26 constant kabatti auxiliary space complexity O(1).
class Solution1:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()

        for char in sentence:
            if char not in seen:
                seen.add(char)

        return len(seen) == 26


# ============================================================


# Approach 2: HashSet with Early Return
# Recommended Current-Level Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Time Explanation:
# Prati character ni set lo add chestunnam.
# Set size 26 ayina ventane remaining characters check cheyakundaa
# True return chestunnam.
# Worst case lo total time complexity O(n).
#
# Space Explanation:
# Set lo maximum 26 lowercase letters maatrame store avutayi.
# Kabatti auxiliary space complexity O(1).
class Solution2:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()

        for char in sentence:
            seen.add(char)

            if len(seen) == 26:
                return True

        return False


# ============================================================


# Approach 3: Boolean Array
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Time Explanation:
# Sentence lo prati character ni okasari process chestunnam.
# Character position calculate chesi boolean array lo mark chestunnam.
# Kabatti total time complexity O(n).
#
# Space Explanation:
# Fixed size 26 boolean values unna array use chestunnam.
# Fixed size kabatti auxiliary space complexity O(1).
class Solution3:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = [False] * 26
        count = 0

        for char in sentence:
            index = ord(char) - ord("a")

            if not letters[index]:
                letters[index] = True
                count += 1

                if count == 26:
                    return True

        return False


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Bitmask
# Recommended Optimal Space Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Time Explanation:
# Prati character kosam corresponding bit ni set chestunnam.
# Anni 26 bits set ayinaayaa ani check chestunnam.
# Kabatti total time complexity O(n).
#
# Space Explanation:
# Oka integer bitmask maatrame use chestunnam.
# Additional collection create cheyadam ledu.
# Kabatti auxiliary space complexity O(1).
class Solution4:
    def checkIfPangram(self, sentence: str) -> bool:
        mask = 0
        all_letters = (1 << 26) - 1

        for char in sentence:
            index = ord(char) - ord("a")
            mask = mask | (1 << index)

            if mask == all_letters:
                return True

        return False


# ============================================================


# Approach 5: Check Every Alphabet Character
# Time Complexity: O(26 * n) = O(n)
# Space Complexity: O(1)
#
# Time Explanation:
# 26 alphabet characters lo prati character sentence lo undaa
# ani membership check chestunnam.
# Oka string membership check O(n) time teesukovachu.
# 26 constant kabatti total time O(26 * n), simplified-ga O(n).
#
# Space Explanation:
# Additional data structure create cheyadam ledu.
# Fixed alphabet string maatrame use chestunnam.
# Kabatti auxiliary space complexity O(1).
class Solution5:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for char in alphabet:
            if char not in sentence:
                return False

        return True


# ============================================================


# Approach 6: Set Conversion
# Shortest Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Time Explanation:
# Complete sentence ni set ga convert cheyadaniki O(n) time padutundi.
# Set length ni 26 tho compare cheyadam O(1).
# Kabatti total time complexity O(n).
#
# Space Explanation:
# Set lo maximum 26 lowercase letters maatrame untayi.
# Kabatti auxiliary space complexity O(1).
class Solution6:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
