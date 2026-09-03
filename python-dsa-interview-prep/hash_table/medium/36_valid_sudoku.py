# LeetCode 36 - Valid Sudoku
# Difficulty: Medium

# Recommended Optimal Approach:
# Single-Pass Row, Column and Box HashSets
#
# Recommended Current-Level Approach:
# Single-Pass Row, Column and Box HashSets

# Given board size is always 9 x 9.
# Kabatti fixed-size board kosam time/space O(1) ani cheptham.
#
# Generalized comparison kosam:
# N = board side length.
# Board size N x N, with sqrt(N) x sqrt(N) boxes ani assume chestham.
# Generalized complexities conceptual comparison kosam maatrame.
# Kinda implementations original 9 x 9 problem kosame.
#
# Dictionary and set operations use average-case complexity.
# Input board storage auxiliary space lo include cheyatledu.
# All implementations preserve the original board.
#
# Important:
# "." empty cell; validation lo ignore cheyali.
# Filled digits repeat kakudadhu.
# Every row/column/box completely filled undalsina avasaram ledu.
# Sudoku solve cheyadam kaadu; existing board validate cheyadam.


from typing import List


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Single-Pass Row, Column and Box HashSets
# Your Approach
# Recommended Optimal and Current-Level Approach
#
# Time Complexity: O(1) for the fixed 9 x 9 board
# Space Complexity: O(1) for the fixed 9 x 9 board
#
# Generalized Time Complexity: O(N^2)
# Generalized Space Complexity: O(N^2)
#
# Time Explanation:
# Maximum 81 cells traverse chestunnam.
# Prati filled cell kosam row, column, box membership check chestunnam.
# Set lookup and insertion average-ga O(1).
# 81 fixed kabatti actual problem time O(1).
# Generalized N x N board ayite O(N^2).
#
# Space Explanation:
# 9 row sets, 9 column sets, 9 box sets untayi.
# Maximum 81 row entries + 81 column entries + 81 box entries.
# Total storage fixed kabatti O(1).
# Generalized board lo all groups data store chestham: O(N^2).
#
# Logic:
# rows[r] -> row r lo already unna digits.
# cols[c] -> column c lo already unna digits.
# boxes[r // 3][c // 3] -> current 3 x 3 box digits.
#
# Example:
# r = 5, c = 7
# row_box = 5 // 3 = 1
# col_box = 7 // 3 = 2
# Current cell boxes[1][2] ki belong avutundi.

class Solution1:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [
            [set() for _ in range(3)]
            for _ in range(3)
        ]

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                row_box = r // 3
                col_box = c // 3

                if value in rows[r]:
                    return False

                if value in cols[c]:
                    return False

                if value in boxes[row_box][col_box]:
                    return False

                rows[r].add(value)
                cols[c].add(value)
                boxes[row_box][col_box].add(value)

        return True


# ============================================================


# Approach 2: Validate Groups Separately Using One Set at a Time
# Lower Auxiliary Space for a Generalized Board
#
# Time Complexity: O(1) for the fixed board
# Space Complexity: O(1) for the fixed board
#
# Generalized Time Complexity: O(N^2)
# Generalized Space Complexity: O(N)
#
# Time Explanation:
# Rows check cheyadaniki maximum 81 cell visits.
# Columns check cheyadaniki maximum 81 cell visits.
# Boxes check cheyadaniki maximum 81 cell visits.
# Total maximum 243 visits; fixed kabatti O(1).
# Generalized board lo 3 * N^2, simplified-ga O(N^2).
#
# Space Explanation:
# Oka group kosam maatrame seen set maintain chestunnam.
# Set lo maximum 9 digits untayi.
# Next group kosam fresh set create chestunnam.
# Actual problem lo O(1); generalized board lo O(N).
#
# Logic:
# First all rows validate cheyali.
# Next all columns validate cheyali.
# Finally all 3 x 3 boxes validate cheyali.
#
# Box starting indices:
# Rows:    0, 3, 6
# Columns: 0, 3, 6

class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows.
        for r in range(9):
            seen = set()

            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # Check columns.
        for c in range(9):
            seen = set()

            for r in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # Check boxes.
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()

                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        value = board[r][c]

                        if value == ".":
                            continue

                        if value in seen:
                            return False

                        seen.add(value)

        return True


# ============================================================


# Approach 3: Boolean Presence Arrays
# Alternative Without Hashing
#
# Time Complexity: O(1) for the fixed board
# Space Complexity: O(1) for the fixed board
#
# Generalized Time Complexity: O(N^2)
# Generalized Space Complexity: O(N^2)
#
# Time Explanation:
# Three 9 x 9 boolean structures initialize chestunnam.
# Tarvata maximum 81 board cells inspect chestunnam.
# Array lookup and update O(1).
# Actual board size fixed kabatti total O(1).
# Generalized board lo initialization and scan O(N^2).
#
# Space Explanation:
# Rows, columns, boxes kosam 81 boolean entries each.
# Total 243 entries fixed kabatti O(1).
# Generalized board lo total O(N^2).
#
# Logic:
# Digit "1" -> index 0.
# Digit "9" -> index 8.
# False -> digit inka aa group lo kanipinchaledu.
# True -> digit already aa group lo undi.
#
# Box ID:
# (r // 3) * 3 + (c // 3)
# Idi 3 x 3 box coordinates ni IDs 0 through 8 ga marustundi.
#
# Example:
# r = 5, c = 7
# box_id = 1 * 3 + 2 = 5.

class Solution3:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                digit = int(value) - 1
                box_id = (r // 3) * 3 + (c // 3)

                if (
                    rows[r][digit]
                    or cols[c][digit]
                    or boxes[box_id][digit]
                ):
                    return False

                rows[r][digit] = True
                cols[c][digit] = True
                boxes[box_id][digit] = True

        return True


# ============================================================
# OTHER USEFUL SOLUTIONS
# ============================================================


# Approach 4: One HashSet with Tagged Tuple Keys
# Compact Single-Pass Approach
#
# Time Complexity: O(1) for the fixed board
# Space Complexity: O(1) for the fixed board
#
# Generalized Time Complexity: O(N^2)
# Generalized Space Complexity: O(N^2)
#
# Time Explanation:
# Maximum 81 cells process chestunnam.
# Prati filled cell kosam three fixed-size tuple keys create chestunnam.
# Membership checks and insertions average-ga O(1).
# Fixed board kosam total O(1).
# Generalized board kosam O(N^2).
#
# Space Explanation:
# Prati filled cell kosam three keys store chestunnam.
# Maximum 81 * 3 = 243 entries.
# Actual problem lo O(1); generalized board lo O(N^2).
#
# Logic:
# Oke set lo different types of information store chestunnam.
# Tags valla row, column, box information separate-ga untundi.
#
# Example keys:
# ("row", 0, "5")
# ("col", 4, "5")
# ("box", 0, 1, "5")
#
# Note:
# Oke set use chestunnam kabatti generalized space O(1) kaadu.
# Container count kaadu; stored entries count mukhyam.

class Solution4:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                row_key = ("row", r, value)
                col_key = ("col", c, value)
                box_key = ("box", r // 3, c // 3, value)

                if (
                    row_key in seen
                    or col_key in seen
                    or box_key in seen
                ):
                    return False

                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        return True


# ============================================================


# Approach 5: Counter + Reusable Group Validator
# Frequency-Based Approach
#
# Time Complexity: O(1) for the fixed board
# Space Complexity: O(1) for the fixed board
#
# Generalized Time Complexity: O(N^2)
# Generalized Space Complexity: O(N)
#
# Time Explanation:
# Total 27 groups validate chestunnam.
# Prati group lo 9 cells maatrame untayi.
# Counter build chesi frequency values check chestunnam.
# Fixed amount of work kabatti O(1).
# Generalized board lo O(N^2).
#
# Space Explanation:
# Oka group Counter lo maximum 9 entries untayi.
# Group validation complete ayyaka Counter retain cheyatledu.
# All groups ni lists ga create chesi store cheyatledu.
# Actual problem lo O(1); generalized board lo O(N).
#
# Logic:
# "." remove chesi filled digits frequencies calculate chestham.
# Prati frequency 1 ayite group valid.
# Completely empty group kuda valid:
# all() empty iterable meeda True istundi.

class Solution5:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import Counter

        def valid_group(values):
            frequency = Counter(
                value
                for value in values
                if value != "."
            )

            return all(
                count == 1
                for count in frequency.values()
            )

        for i in range(9):
            if not valid_group(board[i]):
                return False

            if not valid_group(
                board[r][i]
                for r in range(9)
            ):
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                values = (
                    board[r][c]
                    for r in range(box_row, box_row + 3)
                    for c in range(box_col, box_col + 3)
                )

                if not valid_group(values):
                    return False

        return True


# ============================================================


# Approach 6: Brute Force Comparison Within Each Group
# Constant Auxiliary Space Even for a Generalized Board
#
# Time Complexity: O(1) for the fixed board
# Space Complexity: O(1)
#
# Generalized Time Complexity: O(N^3)
# Generalized Space Complexity: O(1)
#
# Time Explanation:
# Prati filled cell kosam same row, column, box lo values compare chestham.
# Actual board lo cells and group sizes fixed kabatti O(1).
#
# Generalized N x N board lo:
# N^2 cells untayi.
# Prati cell kosam row/column/box comparisons O(N).
# Total O(N^2 * N) = O(N^3).
#
# Space Explanation:
# Additional sets, dictionaries, arrays create cheyatledu.
# Loop variables and temporary coordinates maatrame use chestunnam.
# Kabatti auxiliary space O(1).
#
# Logic:
# Current digit same row, column, box lo malli undaa ani compare chestham.
# Current cell ni danithone compare cheyakudadhu.
# Later cells tho compare chesthe duplicate pairs repeat cheyalsina
# avasaram taggutundi.
#
# Note:
# Fixed board valla O(1) label unna,
# HashSet approaches kanna repeated comparisons ekkuva chestundi.

class Solution6:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                # Compare with later cells in the same row.
                for other_col in range(c + 1, 9):
                    if board[r][other_col] == value:
                        return False

                # Compare with later cells in the same column.
                for other_row in range(r + 1, 9):
                    if board[other_row][c] == value:
                        return False

                # Compare within the same box.
                start_row = (r // 3) * 3
                start_col = (c // 3) * 3

                for other_row in range(start_row, start_row + 3):
                    for other_col in range(start_col, start_col + 3):
                        if (
                            (other_row, other_col) > (r, c)
                            and board[other_row][other_col] == value
                        ):
                            return False

        return True
