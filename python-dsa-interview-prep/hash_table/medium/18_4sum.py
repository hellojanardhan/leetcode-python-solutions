# LeetCode 18 - 4Sum
# Difficulty: Medium
#
# Recommended Optimal Approach:
# Sorting + Two Fixed Indices + Two Pointers
#
# Recommended Current-Level Approach:
# Sorting + Two Fixed Indices + Two Pointers


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Sorting + Two Fixed Indices + Two Pointers
# Your Approach — Recommended Optimal Approach
#
# Time Complexity: O(n³)
# Algorithm Auxiliary Space: O(1)
# Python sorting can use O(n) auxiliary space.
# Output space: O(q), where q is number of quadruplets.

class Solution1:
    def fourSum(
        self,
        nums: List[int],
        target: int
    ) -> List[List[int]]:

        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if (
                    j > i + 1
                    and nums[j] == nums[j - 1]
                ):
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = (
                        nums[i]
                        + nums[j]
                        + nums[left]
                        + nums[right]
                    )

                    if total < target:
                        left += 1

                    elif total > target:
                        right -= 1

                    else:
                        result.append([
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        ])

                        left += 1
                        right -= 1

                        while (
                            left < right
                            and nums[left] == nums[left - 1]
                        ):
                            left += 1

                        while (
                            left < right
                            and nums[right] == nums[right + 1]
                        ):
                            right -= 1

        return result


# ============================================================
# Approach 2: Generalized K-Sum Recursion
#
# Time Complexity for 4Sum: O(n³)
# Recursion Space: O(k)
#
# This approach can also solve 2Sum, 3Sum, 4Sum and K-Sum.
# ============================================================

class Solution2:
    def fourSum(
        self,
        nums: List[int],
        target: int
    ) -> List[List[int]]:

        nums.sort()
        return self.kSum(nums, target, 0, 4)

    def kSum(
        self,
        nums: List[int],
        target: int,
        start: int,
        k: int
    ) -> List[List[int]]:

        result = []
        n = len(nums)

        if n - start < k:
            return result

        if (
            nums[start] * k > target
            or nums[-1] * k < target
        ):
            return result

        if k == 2:
            left = start
            right = n - 1

            while left < right:
                total = nums[left] + nums[right]

                if total < target:
                    left += 1

                elif total > target:
                    right -= 1

                else:
                    result.append([
                        nums[left],
                        nums[right]
                    ])

                    left_value = nums[left]
                    right_value = nums[right]

                    while (
                        left < right
                        and nums[left] == left_value
                    ):
                        left += 1

                    while (
                        left < right
                        and nums[right] == right_value
                    ):
                        right -= 1

            return result

        for i in range(start, n - k + 1):
            if (
                i > start
                and nums[i] == nums[i - 1]
            ):
                continue

            subsets = self.kSum(
                nums,
                target - nums[i],
                i + 1,
                k - 1
            )

            for subset in subsets:
                result.append([nums[i]] + subset)

        return result


# ============================================================
# Approach 3: Two Fixed Indices + HashSet
#
# Time Complexity: O(n³) average
# Space Complexity: O(n + q)
#
# seen contains previous third-number candidates.
# Result set automatically removes duplicate quadruplets.
# ============================================================

class Solution3:
    def fourSum(
        self,
        nums: List[int],
        target: int
    ) -> List[List[int]]:

        nums.sort()
        quadruplets = set()
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if (
                    j > i + 1
                    and nums[j] == nums[j - 1]
                ):
                    continue

                seen = set()

                for k in range(j + 1, n):
                    required = target - (
                        nums[i] + nums[j] + nums[k]
                    )

                    if required in seen:
                        quadruplets.add((
                            nums[i],
                            nums[j],
                            required,
                            nums[k]
                        ))

                    seen.add(nums[k])

        return [
            list(quadruplet)
            for quadruplet in quadruplets
        ]


# ============================================================
# OTHER USEFUL SOLUTIONS
# ============================================================


# Approach 4: Three Loops + Binary Search
#
# Time Complexity: O(n³ log n)
# Auxiliary Space: O(1), excluding sorting/output
#
# Fourth value is searched only after index k.
# ============================================================

class Solution4:
    def fourSum(
        self,
        nums: List[int],
        target: int
    ) -> List[List[int]]:

        from bisect import bisect_left

        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if (
                    j > i + 1
                    and nums[j] == nums[j - 1]
                ):
                    continue

                for k in range(j + 1, n - 1):
                    if (
                        k > j + 1
                        and nums[k] == nums[k - 1]
                    ):
                        continue

                    required = target - (
                        nums[i] + nums[j] + nums[k]
                    )

                    fourth_index = bisect_left(
                        nums,
                        required,
                        k + 1
                    )

                    if (
                        fourth_index < n
                        and nums[fourth_index] == required
                    ):
                        result.append([
                            nums[i],
                            nums[j],
                            nums[k],
                            required
                        ])

        return result


# ============================================================
# Approach 5: Four Nested Loops + Result Set
#
# Time Complexity: O(n⁴)
# Space Complexity: O(q)
#
# Brute-force approach.
# ============================================================

class Solution5:
    def fourSum(
        self,
        nums: List[int],
        target: int
    ) -> List[List[int]]:

        nums.sort()
        result = set()
        n = len(nums)

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    for fourth in range(k + 1, n):
                        total = (
                            nums[i]
                            + nums[j]
                            + nums[k]
                            + nums[fourth]
                        )

                        if total == target:
                            result.add((
                                nums[i],
                                nums[j],
                                nums[k],
                                nums[fourth]
                            ))

        return [
            list(quadruplet)
            for quadruplet in result
        ]
