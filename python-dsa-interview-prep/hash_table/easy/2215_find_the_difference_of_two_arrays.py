# LeetCode 2215 - Find the Difference of Two Arrays
# Difficulty: Easy
#
# Recommended Approach: Two HashSets
# Recommended Current-Level Approach: Two HashSets + Manual Membership


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Two HashSets + Manual Membership
# Your Approach
# Recommended Current-Level Approach
#
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
#
# Time Explanation:
# nums1 and nums2 ni sets ga convert cheyadaniki O(n + m).
# Unique elements ni traverse cheyadaniki O(n + m).
# Set membership average-ga O(1).
#
# Space Explanation:
# Two HashSets and result store chestunnam.
# Kabatti total space O(n + m).

class Solution1:
    def findDifference(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> List[List[int]]:

        seen1 = set(nums1)
        seen2 = set(nums2)

        answer = [[], []]

        for number in seen1:
            if number not in seen2:
                answer[0].append(number)

        for number in seen2:
            if number not in seen1:
                answer[1].append(number)

        return answer


# ============================================================


# Approach 2: Set Difference
# Recommended Short Optimal Approach
#
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

class Solution2:
    def findDifference(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> List[List[int]]:

        seen1 = set(nums1)
        seen2 = set(nums2)

        return [
            list(seen1 - seen2),
            list(seen2 - seen1)
        ]


# ============================================================


# Approach 3: Single HashMap + Presence Flags
#
# Time Complexity: O(n + m)
# Space Complexity: O(u)
#
# Flag 1 → nums1 lo maatrame undi
# Flag 2 → nums2 lo maatrame undi
# Flag 3 → Rendu arrays lo undi

class Solution3:
    def findDifference(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> List[List[int]]:

        presence = {}

        for number in nums1:
            presence[number] = (
                presence.get(number, 0) | 1
            )

        for number in nums2:
            presence[number] = (
                presence.get(number, 0) | 2
            )

        answer = [[], []]

        for number, flag in presence.items():
            if flag == 1:
                answer[0].append(number)

            elif flag == 2:
                answer[1].append(number)

        return answer


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Two Frequency HashMaps
#
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
#
# Correct, but occurrence counts unnecessary.

class Solution4:
    def findDifference(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> List[List[int]]:

        frequency1 = {}
        frequency2 = {}

        for number in nums1:
            frequency1[number] = (
                frequency1.get(number, 0) + 1
            )

        for number in nums2:
            frequency2[number] = (
                frequency2.get(number, 0) + 1
            )

        return [
            [
                number
                for number in frequency1
                if number not in frequency2
            ],
            [
                number
                for number in frequency2
                if number not in frequency1
            ]
        ]


# ============================================================


# Approach 5: Set Iteration + List Membership
# Your Previous Approach
#
# Time Complexity: O(n * m)
# Space Complexity: O(n + m)
#
# List membership repeated-ga linear scan chestundi.
# Kabatti correct, kaani optimal kaadu.

class Solution5:
    def findDifference(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> List[List[int]]:

        answer = [[], []]

        for number in set(nums1):
            if number not in nums2:
                answer[0].append(number)

        for number in set(nums2):
            if number not in nums1:
                answer[1].append(number)

        return answer
