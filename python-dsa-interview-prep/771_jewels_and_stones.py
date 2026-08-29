# LeetCode 771 - Jewels and Stones
# Difficulty: Easy

# Recommended Approach: HashSet + Linear Scan
# Recommended Current-Level Approach: HashSet + Linear Scan


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: HashSet + Linear Scan
# Recommended Optimal Approach
# Time Complexity: O(j + s)
# Space Complexity: O(j)
#
# Time Explanation:
# jewels ni set ga convert cheyadaniki O(j) time padutundi.
# stones lo unna prati character ni okasari traverse chestunnam.
# Set membership check average-ga O(1).
# Kabatti total time complexity O(j + s).
#
# Space Explanation:
# jewels unique characters ni set lo store chestunnam.
# Worst case lo j characters store avutayi.
# Kabatti auxiliary space complexity O(j).
class Solution1:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        count = 0

        for stone in stones:
            if stone in jewel_set:
                count += 1

        return count


# ============================================================


# Approach 2: HashSet + Generator Expression
# Short Optimal Approach
# Time Complexity: O(j + s)
# Space Complexity: O(j)
#
# Time Explanation:
# jewels ni set ga convert cheyadaniki O(j).
# stones lo prati character ni okasari check cheyadaniki O(s).
# Kabatti total time complexity O(j + s).
#
# Space Explanation:
# Jewel set lo maximum j unique characters store avutayi.
# Generator separate list create cheyadu.
# Kabatti auxiliary space complexity O(j).
class Solution2:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)

        return sum(stone in jewel_set for stone in stones)


# ============================================================


# Approach 3: count() for Every Jewel
# Your Approach
# Time Complexity: O(j + u * s)
# Space Complexity: O(j)
#
# Time Explanation:
# jewels ni set ga convert cheyadaniki O(j).
# u unique jewels lo prati jewel kosam stones.count() complete
# stones string ni scan chestundi.
# Kabatti total time complexity O(j + u * s).
# Worst case lo idi O(j * s).
#
# Space Explanation:
# set(jewels) lo unique jewel characters store avutayi.
# Worst case lo j characters store avutayi.
# Kabatti auxiliary space complexity O(j).
class Solution3:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_count = 0

        for jewel in set(jewels):
            stones_count += stones.count(jewel)

        return stones_count


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Direct String Membership
# Time Complexity: O(j * s)
# Space Complexity: O(1)
#
# Time Explanation:
# stones lo prati character kosam jewels string lo search chestunnam.
# String membership worst case lo O(j) time teesukuntundi.
# Ee check s stones kosam jarugutundi.
# Kabatti total time complexity O(j * s).
#
# Space Explanation:
# Additional set, dictionary ledaa list create cheyadam ledu.
# Count variable maatrame use chestunnam.
# Kabatti auxiliary space complexity O(1).
class Solution4:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0

        for stone in stones:
            if stone in jewels:
                count += 1

        return count


# ============================================================


# Approach 5: Nested Loops
# Time Complexity: O(j * s)
# Space Complexity: O(1)
#
# Time Explanation:
# Prati stone ni prati jewel tho compare chestunnam.
# Worst case lo s * j comparisons jarugutayi.
# Kabatti total time complexity O(j * s).
#
# Space Explanation:
# Additional data structure create cheyadam ledu.
# Count variable maatrame use chestunnam.
# Kabatti auxiliary space complexity O(1).
class Solution5:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0

        for stone in stones:
            for jewel in jewels:
                if stone == jewel:
                    count += 1
                    break

        return count
