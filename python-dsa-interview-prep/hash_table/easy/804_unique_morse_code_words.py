# LeetCode 804 - Unique Morse Code Words
# Difficulty: Easy
# Recommended Approach: HashSet + Morse Transformation
# Recommended Current-Level Approach: HashSet + Morse Transformation


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: HashSet + Build Morse String
# Your Approach
# Time Complexity: O(C) conceptually
# Space Complexity: O(W + C)
#
# C = total number of characters across all words
# W = number of unique Morse transformations
#
# Time Explanation:
# Prati word lo prati character ni okasari traverse chestunnam.
# ord(char) - ord("a") use chesi Morse code direct-ga lookup chestunnam.
# Set insertion average-ga O(1).
# Morse code length maximum fixed size kabatti conceptual DSA analysis lo
# total traversal O(C).
#
# Python lo repeated string += immutable strings create cheyyachu,
# kabatti long strings case lo extra copying jaragachu.
# Anduke Approach 2 cleaner.
#
# Space Explanation:
# seen set lo unique transformed Morse strings store chestunnam.
# Kabatti transformed data size ki proportional-ga space use avutundi.
class Solution1:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
            "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
            "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
            "-.--", "--.."
        ]

        seen = set()

        for word in words:
            result = ""

            for char in word:
                result += morse[ord(char) - ord("a")]

            seen.add(result)

        return len(seen)


# ============================================================


# Approach 2: HashSet + List + join()
# Recommended Optimal Python Approach
# Time Complexity: O(C)
# Space Complexity: O(W + C)
#
# Time Explanation:
# Prati character ni exactly once process chestunnam.
# Character Morse representation ni list lo append chestunnam.
# Finally join() transformed word ni linear time lo build chestundi.
# Kabatti total time complexity O(C).
#
# Space Explanation:
# Current word transformation kosam temporary list use chestunnam.
# Unique transformed strings seen set lo store chestunnam.
# Kabatti overall space transformed input size ki proportional.
class Solution2:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
            "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
            "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
            "-.--", "--.."
        ]

        seen = set()

        for word in words:
            encoded = []

            for char in word:
                encoded.append(
                    morse[ord(char) - ord("a")]
                )

            seen.add("".join(encoded))

        return len(seen)


# ============================================================


# Approach 3: Set Comprehension + join()
# Short Pythonic Approach
# Time Complexity: O(C)
# Space Complexity: O(W + C)
#
# Time Explanation:
# Each word characters ni Morse representation ki convert chesi
# join() tho transformed string build chestunnam.
# All words total characters C kabatti O(C).
#
# Space Explanation:
# Unique Morse transformations set lo store avutayi.
# Kabatti transformed output size ki proportional space use avutundi.
class Solution3:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
            "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
            "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
            "-.--", "--.."
        ]

        transformations = {
            "".join(
                morse[ord(char) - ord("a")]
                for char in word
            )
            for word in words
        }

        return len(transformations)


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Dictionary Character -> Morse Mapping
# Time Complexity: O(C)
# Space Complexity: O(W + C)
#
# Time Explanation:
# Character ki Morse value dictionary nundi average O(1) lo lookup chestunnam.
# Total characters C ni process chestunnam.
# Kabatti O(C).
#
# Space Explanation:
# Morse mapping fixed 26 entries.
# Unique transformations set lo store chestunnam.
class Solution4:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
            "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
            "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
            "-.--", "--.."
        ]

        morse_map = {
            chr(ord("a") + i): codes[i]
            for i in range(26)
        }

        seen = set()

        for word in words:
            encoded = "".join(
                morse_map[char]
                for char in word
            )

            seen.add(encoded)

        return len(seen)
