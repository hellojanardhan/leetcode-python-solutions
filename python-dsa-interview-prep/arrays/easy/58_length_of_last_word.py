# LeetCode 58 - Length of Last Word
# Difficulty: Easy
# Recommended Approach: Reverse Linear Scan
# Recommended Current-Level Approach: Reverse Linear Scan


# Approach 1: Reverse Linear Scan - Optimal Solution
# Time Complexity: O(n)
# String ni last nunchi backward ga scan chesthunnam. Worst case lo n characters ni check chestham.
# Space Complexity: O(1)
# count mariyu i variables mathrame use chesthunnam.
class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        count = 0

        while i >= 0 and s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            count += 1
            i -= 1

        return count


# Approach 2: Using split()
# Time Complexity: O(n)
# split() complete string lo unna characters ni process chesthundi.
# Space Complexity: O(n)
# Words ni store cheyadaniki kottha list create chesthundi.
class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()

        return len(words[-1])


# Approach 3: Your Approach - split(" ") and List Comprehension
# Time Complexity: O(n)
# split() mariyu list comprehension complete string ni process chesthayi.
# Space Complexity: O(n)
# l mariyu result ane rendu additional lists create chesthunnam.
class Solution3:
    def lengthOfLastWord(self, s: str) -> int:
        words_with_empty_strings = s.split(" ")
        words = [word for word in words_with_empty_strings if word != ""]

        return len(words[-1])


# Approach 4: Using rstrip() and split()
# Time Complexity: O(n)
# rstrip() trailing spaces remove chesthundi, split() words ni separate chesthundi.
# Space Complexity: O(n)
# Trimmed string mariyu words list additional ga create avuthayi.
class Solution4:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.rstrip().split(" ")

        return len(words[-1])


# Approach 5: Using rsplit()
# Time Complexity: O(n)
# rsplit() right side nunchi last word ni separate chesthundi.
# Space Complexity: O(n)
# String parts ni store cheyadaniki additional list create avuthundi.
class Solution5:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.rsplit(maxsplit=1)[-1]

        return len(last_word)
