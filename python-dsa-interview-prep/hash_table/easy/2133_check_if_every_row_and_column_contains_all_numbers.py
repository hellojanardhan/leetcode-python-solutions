# LeetCode 2133 - Check if Every Row and Column Contains All Numbers
# Difficulty: Easy

# Recommended Optimal Approach: Row and Column HashSets
# Recommended Current-Level Approach: Row and Column HashSets

# n = number of rows = number of columns
#
# Problem constraints:
# Matrix size n x n.
# Every value is between 1 and n.
#
# Important:
# Oka row/column lo n values undi duplicates lekapothe,
# 1 nunchi n varaku anni numbers unnatte.
#
# Dictionary and set operations use average-case complexity.
# Space complexities exclude the input matrix.
# All approaches below preserve the original matrix.


from typing import List


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Row and Column HashSets
# Previously Explained Approach
# Recommended Time-Optimal Approach
# Time Complexity: O(n^2)
# Space Complexity: O(n)
#
# Time Explanation:
# Outer loop n times run avutundi.
# Prati outer iteration lo inner loop n times run avutundi.
# Row and column values ni set lo check chestunnam.
# Set lookup and insertion average-ga O(1).
# Total n * n = O(n^2).
#
# Space Explanation:
# row_seen lo maximum n values untayi.
# column_seen lo maximum n values untayi.
# Prati outer iteration ki fresh sets create chestunnam.
# Previous rows/columns sets ni store chesthu vellatledu.
# Peak additional space O(n + n), simplified-ga O(n).
#
# Logic:
# matrix[i][j] -> row i lo values.
# matrix[j][i] -> column i lo values.
# Same row/column lo duplicate dorikite False.
#
# Example:
# matrix = [[1,2,3], [3,1,2], [2,3,1]]
#
# i = 0:
# Row values    = [1,2,3]
# Column values = [1,3,2]
# Rendu groups lo duplicates levu.

class Solution1:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for i in range(n):
            row_seen = set()
            column_seen = set()

            for j in range(n):
                row_value = matrix[i][j]
                column_value = matrix[j][i]

                if row_value in row_seen:
                    return False

                if column_value in column_seen:
                    return False

                row_seen.add(row_value)
                column_seen.add(column_value)

        return True


# ============================================================


# Approach 2: Separate Row and Column Frequency HashMaps
# Your Frequency Idea — Corrected
# Time Complexity: O(n^2)
# Space Complexity: O(n)
#
# Time Explanation:
# n rows/columns kosam outer loop run chestunnam.
# Prati iteration lo n values process chestunnam.
# Dictionary lookup and update average-ga O(1).
# Total O(n^2).
#
# Space Explanation:
# Row frequency dictionary lo maximum n entries untayi.
# Column frequency dictionary lo maximum n entries untayi.
# Prati outer iteration ki dictionaries reset chestunnam.
# Total peak additional space O(n).
#
# Logic:
# Prati row/column ki separate frequency dictionary maintain chestham.
# Oka number count 1 kante ekkuva ayite duplicate unnatte.
# Kabatti immediately False return chestham.
#
# Important:
# Complete matrix frequency calculate cheyadam kaadu.
# Prati row and column ni separate-ga validate cheyali.
#
# Example:
# Row [1,2,3] -> {1:1, 2:1, 3:1} -> valid.
# Row [1,1,3] -> count of 1 becomes 2 -> invalid.

class Solution2:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for i in range(n):
            row_frequency = {}
            column_frequency = {}

            for j in range(n):
                row_value = matrix[i][j]
                column_value = matrix[j][i]

                row_frequency[row_value] = (
                    row_frequency.get(row_value, 0) + 1
                )

                column_frequency[column_value] = (
                    column_frequency.get(column_value, 0) + 1
                )

                if (
                    row_frequency[row_value] > 1
                    or column_frequency[column_value] > 1
                ):
                    return False

        return True


# ============================================================


# Approach 3: Boolean Seen Arrays
# Useful Because Values Are Restricted to 1 Through n
# Time Complexity: O(n^2)
# Space Complexity: O(n)
#
# Time Explanation:
# Prati outer iteration lo rendu n + 1 arrays create chestunnam: O(n).
# Tarvata n row/column values process chestunnam: O(n).
# Array lookup and update O(1).
# n outer iterations kosam total O(n * (n + n)) = O(n^2).
#
# Space Explanation:
# Rendu boolean arrays lo n + 1 entries each untayi.
# Previous arrays ni store chesthu vellatledu.
# Total peak additional space O(n).
#
# Logic:
# Array index = number.
# False = number inka ee group lo kanipinchaledu.
# True  = number already ee group lo kanipinchindi.
#
# Note:
# Index 0 use cheyamu.
# n + 1 size valla index n ni access cheyavachu.
# Array size n tho perugutundi kabatti space O(1) kaadu.

class Solution3:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for i in range(n):
            row_seen = [False] * (n + 1)
            column_seen = [False] * (n + 1)

            for j in range(n):
                row_value = matrix[i][j]
                column_value = matrix[j][i]

                if row_seen[row_value] or column_seen[column_value]:
                    return False

                row_seen[row_value] = True
                column_seen[column_value] = True

        return True


# ============================================================
# OTHER USEFUL SOLUTIONS
# ============================================================


# Approach 4: Expected Set + all() + zip()
# Short Python Approach
# Time Complexity: O(n^2)
# Space Complexity: O(n)
#
# Time Explanation:
# Expected set create cheyadaniki O(n).
# Prati row ni set ga convert chesi compare cheyadaniki O(n).
# n rows kosam O(n^2).
# Columns kosam kuda O(n^2).
# Total O(n + n^2 + n^2), simplified-ga O(n^2).
#
# Space Explanation:
# Expected set O(n).
# Oka row/column set kosam O(n).
# zip iterator and current column tuple kosam O(n).
# All column tuples ni list lo store cheyatledu.
# Total peak additional space O(n).
#
# Logic:
# Expected numbers = {1, 2, ..., n}.
# Prati row and column set expected set ki equal undali.
# all() anni checks True ayinappude True istundi.
#
# zip(*matrix):
# Corresponding row positions ni group chesi columns istundi.
#
# Example:
# [[1,2,3], [3,1,2], [2,3,1]]
#
# Columns:
# (1,3,2)
# (2,1,3)
# (3,2,1)

class Solution4:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        expected = set(range(1, n + 1))

        return (
            all(
                set(row) == expected
                for row in matrix
            )
            and all(
                set(column) == expected
                for column in zip(*matrix)
            )
        )


# ============================================================


# Approach 5: Sort Each Row and Column
# Correct but Not Time-Optimal
# Time Complexity: O(n^2 log n)
# Space Complexity: O(n)
#
# Time Explanation:
# Oka row of length n sort cheyadaniki O(n log n).
# Oka column of length n sort cheyadaniki O(n log n).
# Sorted lists compare cheyadaniki O(n).
# Ila n rows/columns process chestunnam.
# Total O(n * n log n) = O(n^2 log n).
#
# Space Explanation:
# Expected list kosam O(n).
# Current sorted row and column kosam O(n).
# Python sorting temporary storage worst-case O(n).
# Anni sorted rows/columns ni kalipi store cheyatledu.
# Total peak additional space O(n).
#
# Logic:
# Valid row/column sort cheste [1, 2, ..., n] ravali.
# Expected list tho compare chestunnam.
#
# Note:
# sorted() kotta list create chestundi.
# Original matrix ni modify cheyadu.

class Solution5:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        expected = list(range(1, n + 1))

        for i in range(n):
            sorted_row = sorted(matrix[i])

            sorted_column = sorted(
                matrix[j][i]
                for j in range(n)
            )

            if (
                sorted_row != expected
                or sorted_column != expected
            ):
                return False

        return True


# ============================================================


# Approach 6: Brute Force Pairwise Comparison
# Constant Auxiliary Space, Slower Approach
# Time Complexity: O(n^3)
# Space Complexity: O(1)
#
# Time Explanation:
# Prati row lo possible pairs ni compare chestunnam.
# Oka row lo n * (n - 1) / 2 pairs untayi: O(n^2).
# Corresponding column kosam kuda same number of comparisons.
# n rows/columns kosam total O(n * n^2) = O(n^3).
#
# Space Explanation:
# Additional sets, dictionaries, arrays create cheyatledu.
# n, i, j, k variables maatrame use chestunnam.
# Kabatti auxiliary space O(1).
#
# Logic:
# Oka row/column lo current value ni later values tho compare chestham.
# Equal pair dorikite duplicate unnatte.
# k = j + 1 nunchi start cheyadam valla self-comparison undadu.
#
# Note:
# Values already 1 through n madhyalo unnayane constraint meeda
# duplicate-only validation depend avutundi.

class Solution6:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                for k in range(j + 1, n):
                    if matrix[i][j] == matrix[i][k]:
                        return False

                    if matrix[j][i] == matrix[k][i]:
                        return False

        return True
