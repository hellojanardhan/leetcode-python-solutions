# LeetCode 349 - Intersection of Two Arrays
# Difficulty: Easy

# Recommended Approach: HashSet Using Smaller List
# Recommended Current-Level Approach: HashSet Lookup + Remove


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: HashSet Lookup + Remove
# Your Approach
# Recommended Current-Level Approach
# Time Complexity: O(n + m)
# Space Complexity: O(n)
#
# Time Explanation:
# nums1 ni set ga convert cheyadaniki O(n) time padutundi.
# nums2 lo unna m elements ni okasari traverse chestunnam.
# Set lookup mariyu remove average-ga O(1) untayi.
# Kabatti total time complexity O(n + m).
#
# Space Explanation:
# nums1 unique values ni seen set lo store chestunnam.
# Worst case lo n values store avutayi.
# Kabatti auxiliary space complexity O(n).
class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        result = []

        for num in nums2:
            if num in seen:
                result.append(num)
                seen.remove(num)

        return result


# ============================================================


# Approach 2: HashSet Using Smaller List
# Recommended Optimal Approach
# Time Complexity: O(n + m)
# Space Complexity: O(min(n, m))
#
# Time Explanation:
# Smaller list ni set ga convert chestunnam.
# Larger list ni okasari traverse chestunnam.
# Set lookup mariyu remove average-ga O(1) untayi.
# Kabatti total time complexity O(n + m).
#
# Space Explanation:
# Smaller list values maatrame set lo store chestunnam.
# Kabatti auxiliary space complexity O(min(n, m)).
class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) <= len(nums2):
            smaller_list = nums1
            larger_list = nums2
        else:
            smaller_list = nums2
            larger_list = nums1

        seen = set(smaller_list)
        result = []

        for num in larger_list:
            if num in seen:
                result.append(num)
                seen.remove(num)

        return result


# ============================================================


# Approach 3: Sorting + Two Pointers
# Time Complexity: O(n log n + m log m)
# Space Complexity: O(n + m)
#
# Time Explanation:
# nums1 ni sort cheyadaniki O(n log n) time padutundi.
# nums2 ni sort cheyadaniki O(m log m) time padutundi.
# Tarvata two pointers tho rendu lists ni scan cheyadaniki O(n + m).
# Kabatti total time O(n log n + m log m).
#
# Space Explanation:
# sorted() rendu kotta lists create chestundi.
# Andulo total n + m elements store avutayi.
# Kabatti auxiliary space complexity O(n + m).
class Solution3:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)

        result = []
        i = 0
        j = 0

        while i < len(sorted_nums1) and j < len(sorted_nums2):
            if sorted_nums1[i] < sorted_nums2[j]:
                i += 1

            elif sorted_nums1[i] > sorted_nums2[j]:
                j += 1

            else:
                if not result or result[-1] != sorted_nums1[i]:
                    result.append(sorted_nums1[i])

                i += 1
                j += 1

        return result


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Two HashSets
# Time Complexity: O(n + m)
# Space Complexity: O(n + k)
#
# Time Explanation:
# nums1 values ni lookup set lo store cheyadaniki O(n).
# nums2 values ni okasari traverse cheyadaniki O(m).
# Set lookup mariyu add average-ga O(1).
# Kabatti total time complexity O(n + m).
#
# Space Explanation:
# lookup set lo nums1 unique values store avutayi.
# result_set lo k common unique values store avutayi.
# Kabatti auxiliary space complexity O(n + k).
class Solution4:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = set()
        result_set = set()

        for num in nums1:
            lookup.add(num)

        for num in nums2:
            if num in lookup:
                result_set.add(num)

        return list(result_set)


# ============================================================


# Approach 5: Built-in Set Intersection Operator
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
#
# Time Explanation:
# Rendu lists ni sets ga convert cheyadaniki O(n + m).
# Set intersection common unique values ni find chestundi.
# Kabatti average total time complexity O(n + m).
#
# Space Explanation:
# nums1 mariyu nums2 kosam separate sets create chestunnam.
# Kabatti auxiliary space complexity O(n + m).
class Solution5:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


# ============================================================


# Approach 6: Built-in intersection()
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
#
# Time Explanation:
# Rendu input lists ni sets ga convert chestunnam.
# intersection() common unique values ni return chestundi.
# Kabatti average total time complexity O(n + m).
#
# Space Explanation:
# Rendu sets create chestunnam.
# Kabatti auxiliary space complexity O(n + m).
class Solution6:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1.intersection(set2))


# ============================================================


# Approach 7: Brute Force + Seen Set
# Time Complexity: O(n * m)
# Space Complexity: O(k)
#
# Time Explanation:
# nums1 lo prati number kosam nums2 lo membership check chestunnam.
# List membership check worst case lo O(m).
# Ee check n numbers kosam jarugutundi.
# Kabatti total time complexity O(n * m).
#
# Space Explanation:
# seen set lo common unique values maatrame store chestunnam.
# k common unique values unte auxiliary space complexity O(k).
class Solution7:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        result = []

        for num in nums1:
            if num in nums2 and num not in seen:
                result.append(num)
                seen.add(num)

        return result


# ============================================================


# Approach 8: Pure Brute Force Without Set
# Time Complexity: O(n * m * k)
# Space Complexity: O(1) Auxiliary
#
# Time Explanation:
# nums1 lo prati number kosam nums2 lo search chestunnam.
# Common number dorikite result lo already undaa ani malli check chestunnam.
# List membership checks repeated ga jarugutayi.
# Kabatti worst-case time complexity O(n * m * k).
#
# Space Explanation:
# Input processing kosam additional set or dictionary create cheyadam ledu.
# Output result list ni auxiliary space calculation lo count cheyadam ledu.
# Kabatti auxiliary space complexity O(1).
class Solution8:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    if num1 not in result:
                        result.append(num1)

                    break

        return result
