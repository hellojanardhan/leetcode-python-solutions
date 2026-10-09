# LeetCode 455 - Assign Cookies
# Difficulty: Easy

# Recommended Approach:
# Sorting + Two Pointers
#
# Recommended Current-Level Approach:
# Sorting + Two Pointers
#
# Main Strategy:
# Greedy
#
# LeetCode Topics:
# Array
# Two Pointers
# Greedy
# Sorting
# QuickSort


# ============================================================
# TOP APPROACHES
# ============================================================


# Approach 1: Sorting + Two Pointers
# Your Approach
# Recommended Current-Level Approach
# Recommended Optimal Approach
#
# Pattern:
# Two Pointers + Greedy + Sorting
#
# Time Complexity:
# O(n log n + m log m)
#
# Space Complexity:
# O(1) excluding sorting internals
#
# Time Explanation:
# First greed array ni ascending order lo
# sort chestunnam.
#
# Cookie sizes ni kuda ascending order lo
# sort chestunnam.
#
# g pointer:
# current smallest unsatisfied child.
#
# s pointer:
# current smallest available cookie.
#
# size[s] >= greed[g] ayite,
# current cookie child ni satisfy chestundi.
#
# Appudu:
# count += 1
# g += 1
#
# Cookie satisfy chesina or cheyyakapoyina,
# current cookie ni malli use cheyyakudadhu.
#
# Kabatti prati iteration lo:
# s += 1
#
# Sorting:
# O(n log n + m log m)
#
# Two-pointer traversal:
# O(n + m)
#
# Total:
# O(n log n + m log m)
#
# Space Explanation:
# g, s, count variables maatrame
# extra ga use chestunnam.
#
# Sorting internal memory ignore chesthe:
# O(1).

class Solution1:
    def findContentChildren(
        self,
        greed: list[int],
        size: list[int]
    ) -> int:

        greed.sort()
        size.sort()

        g = 0
        s = 0
        count = 0

        while (
            g < len(greed)
            and s < len(size)
        ):

            if size[s] >= greed[g]:
                count += 1
                g += 1

            s += 1

        return count


# ============================================================


# Approach 2: Greedy + Sorting
# Pattern:
# Greedy + Sorting
#
# Time Complexity:
# O(n log n + m log m)
#
# Space Complexity:
# O(1) excluding sorting internals
#
# Time Explanation:
# Main greedy rule:
#
# Smallest greed child ki
# smallest sufficient cookie assign cheyyali.
#
# Rendu arrays ni sort chestham.
#
# Prati cookie ni smallest unsatisfied child tho
# compare chestham.
#
# cookie >= greed ayite,
# child satisfied.
#
# child += 1
#
# Cookie too small ayite,
# cookie ni skip chestham.
#
# Enduku safe?
#
# Current smallest child ni kuda
# aa cookie satisfy cheyyalekapothe,
# future children greed values inka
# equal or bigger untayi.
#
# Kabatti aa cookie future lo use avvadu.
#
# Sorting:
# O(n log n + m log m)
#
# Scan:
# O(m)
#
# Total:
# O(n log n + m log m)
#
# Space Explanation:
# child variable maatrame extra.
#
# Sorting internals ignore chesthe:
# O(1).

class Solution2:
    def findContentChildren(
        self,
        g: list[int],
        s: list[int]
    ) -> int:

        g.sort()
        s.sort()

        child = 0

        for cookie in s:

            if child == len(g):
                break

            if cookie >= g[child]:
                child += 1

        return child


# ============================================================


# Approach 3: Array Brute Force
# Pattern:
# Array + Simulation
#
# Time Complexity:
# O(n * m)
#
# Space Complexity:
# O(m)
#
# Time Explanation:
# Prati child kosam,
# cookies anni check chestunnam.
#
# Child ni satisfy chese
# smallest unused cookie ni search chestham.
#
# Prati child ki worst case lo
# m cookies scan cheyyachu.
#
# n children unnaru.
#
# Kabatti:
# O(n * m)
#
# Space Explanation:
# Oka cookie already use ayyinda leda ani
# track cheyyadaniki used array maintain chestham.
#
# used array size = m.
#
# Kabatti:
# O(m).

class Solution3:
    def findContentChildren(
        self,
        g: list[int],
        s: list[int]
    ) -> int:

        used = [False] * len(s)
        count = 0

        for greed in g:

            best_index = -1
            best_size = float("inf")

            for i in range(len(s)):

                if used[i]:
                    continue

                if (
                    s[i] >= greed
                    and s[i] < best_size
                ):
                    best_size = s[i]
                    best_index = i

            if best_index != -1:
                used[best_index] = True
                count += 1

        return count


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Sorting + Binary Search
# Pattern:
# Sorting + Binary Search
#
# Time Complexity:
# O(n log m + n * m)
# in Python list implementation
#
# Space Complexity:
# O(1) excluding sorting internals
#
# Time Explanation:
# Cookies ni ascending order lo sort chestham.
#
# Prati child kosam,
# first cookie >= greed ni
# binary search tho find chestham.
#
# bisect_left:
# O(log m)
#
# Suitable cookie dorikithe,
# aa cookie ni list nunchi remove chestham.
#
# Python list pop(index):
# O(m)
#
# Kabatti overall worst-case:
# O(n * m)
#
# Binary search use chesthunna kuda,
# middle nunchi list element remove cheyyadam
# expensive.
#
# Anduke ee approach
# Two Pointers kanna better kaadu.
#
# Space Explanation:
# Extra major data structure create cheyyatledu.
#
# Sorting internals ignore chesthe:
# O(1).

from bisect import bisect_left


class Solution4:
    def findContentChildren(
        self,
        g: list[int],
        s: list[int]
    ) -> int:

        g.sort()
        s.sort()

        count = 0

        for greed in g:

            index = bisect_left(
                s,
                greed
            )

            if index < len(s):
                count += 1
                s.pop(index)

        return count


# ============================================================


# Approach 5: Explicit QuickSort + Two Pointers
# Pattern:
# QuickSort + Two Pointers + Greedy
#
# Average Time Complexity:
# O(n log n + m log m)
#
# Worst Time Complexity:
# O(n^2 + m^2)
#
# Average Space Complexity:
# O(log n + log m)
#
# Time Explanation:
# Python built-in sort() badulu,
# QuickSort manually implement chestunnam.
#
# First greed array ni QuickSort chestham.
# Tarvata cookies ni QuickSort chestham.
#
# Sorting complete ayyaka,
# same Two Pointer greedy matching
# perform chestham.
#
# QuickSort average:
# O(n log n + m log m)
#
# Matching:
# O(n + m)
#
# Kabatti average total:
# O(n log n + m log m)
#
# Worst case lo bad pivot selection valla:
# O(n^2 + m^2)
#
# Space Explanation:
# QuickSort recursion stack use chestundi.
#
# Average recursion:
# O(log n + log m)
#
# Worst case:
# O(n + m).

class Solution5:
    def findContentChildren(
        self,
        g: list[int],
        s: list[int]
    ) -> int:

        def quicksort(
            arr,
            low,
            high
        ):
            if low >= high:
                return

            pivot = arr[high]
            p = low

            for i in range(
                low,
                high
            ):
                if arr[i] <= pivot:
                    arr[p], arr[i] = (
                        arr[i],
                        arr[p]
                    )
                    p += 1

            arr[p], arr[high] = (
                arr[high],
                arr[p]
            )

            quicksort(
                arr,
                low,
                p - 1
            )

            quicksort(
                arr,
                p + 1,
                high
            )

        quicksort(
            g,
            0,
            len(g) - 1
        )

        quicksort(
            s,
            0,
            len(s) - 1
        )

        child = 0
        cookie = 0

        while (
            child < len(g)
            and cookie < len(s)
        ):

            if s[cookie] >= g[child]:
                child += 1

            cookie += 1

        return child


# ============================================================
# PATTERN SUMMARY
# ============================================================


# Array:
# Brute-force / simulation solution.
#
# Two Pointers:
# Your current solution.
#
# Greedy:
# Smallest child ki
# smallest sufficient cookie assign chestham.
#
# Sorting:
# Children and cookies ni ascending order lo
# arrange cheyyadam.
#
# QuickSort:
# Sorting ni manually implement cheyyadaniki
# one possible sorting algorithm.
#
# Important:
# Sorting and QuickSort alone
# matching strategy kaavu.
#
# Main optimal combination:
#
# Sorting
# +
# Greedy
# +
# Two Pointers
