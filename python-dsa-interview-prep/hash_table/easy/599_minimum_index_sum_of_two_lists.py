# Difficulty: Easy
#
# Recommended Approach:
# HashMap — Word to Index + Running Minimum
#
# Recommended Current-Level Approach:
# HashMap — Word to Index + Running Minimum


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: HashMap + Running Minimum
# Recommended Optimal Approach
#
# Time Complexity: O(n + m)
# Space Complexity: O(m + r)
#
# Time Explanation:
# list2 words and indices HashMap lo store cheyadaniki O(m).
# list1 ni okasari traverse cheyadaniki O(n).
# Dictionary lookup average-ga O(1).
# Total O(n + m).
#
# Space Explanation:
# list2 lo m words HashMap lo store chestunnam.
# Result lo r answer strings store avutayi.
# Output exclude cheste auxiliary space O(m).

class Solution1:
    def findRestaurant(
        self,
        list1: List[str],
        list2: List[str]
    ) -> List[str]:

        word_to_index = {}

        for index, word in enumerate(list2):
            word_to_index[word] = index

        minimum_sum = float("inf")
        result = []

        for index, word in enumerate(list1):
            if word not in word_to_index:
                continue

            current_sum = index + word_to_index[word]

            if current_sum < minimum_sum:
                minimum_sum = current_sum
                result = [word]

            elif current_sum == minimum_sum:
                result.append(word)

        return result


# ============================================================


# Approach 2: Store the Smaller List in HashMap
# Optimal Time + Better Practical Space
#
# Time Complexity: O(n + m)
# Space Complexity: O(min(n, m) + r)
#
# Space Explanation:
# Smaller list words maatrame dictionary lo store chestunnam.
# Kabatti HashMap space O(min(n, m)).

class Solution2:
    def findRestaurant(
        self,
        list1: List[str],
        list2: List[str]
    ) -> List[str]:

        if len(list1) > len(list2):
            list1, list2 = list2, list1

        word_to_index = {
            word: index
            for index, word in enumerate(list1)
        }

        minimum_sum = float("inf")
        result = []

        for index, word in enumerate(list2):
            if word not in word_to_index:
                continue

            current_sum = index + word_to_index[word]

            if current_sum < minimum_sum:
                minimum_sum = current_sum
                result = [word]

            elif current_sum == minimum_sum:
                result.append(word)

        return result


# ============================================================


# Approach 3: Two HashMaps + Common Words
#
# Time Complexity: O(n + m)
# Space Complexity: O(n + m + r)
#
# Time Explanation:
# Rendu lists kosam index dictionaries build chestunnam.
# Common words ni average O(n + m) time lo identify chestunnam.
#
# Space Explanation:
# Rendu lists indices dictionaries lo store chestunnam.
# Problem solve cheyadaniki two dictionaries necessary kaavu,
# kaani approach correct and time-optimal.

class Solution3:
    def findRestaurant(
        self,
        list1: List[str],
        list2: List[str]
    ) -> List[str]:

        first_indices = {
            word: index
            for index, word in enumerate(list1)
        }

        second_indices = {
            word: index
            for index, word in enumerate(list2)
        }

        common_words = (
            first_indices.keys()
            & second_indices.keys()
        )

        minimum_sum = min(
            first_indices[word] + second_indices[word]
            for word in common_words
        )

        return [
            word
            for word in common_words
            if (
                first_indices[word]
                + second_indices[word]
                == minimum_sum
            )
        ]


# ============================================================
# OTHER USEFUL SOLUTIONS
# ============================================================


# Approach 4: Membership + index()
# Your Approach — Cleaned
#
# Time Complexity: O(n * m)
# Space Complexity: O(c + r)
#
# Time Explanation:
# list1 lo prati word kosam:
#
# word in list2  → O(m)
# list2.index()  → O(m)
#
# Worst case:
# n * (m + m) = O(n * m)
#
# Logic correct, kaani list2 repeated-ga scan avutundi.

class Solution4:
    def findRestaurant(
        self,
        list1: List[str],
        list2: List[str]
    ) -> List[str]:

        index_sums = {}

        for index, word in enumerate(list1):
            if word in list2:
                index_sums[word] = (
                    index + list2.index(word)
                )

        minimum_sum = min(index_sums.values())

        return [
            word
            for word, index_sum in index_sums.items()
            if index_sum == minimum_sum
        ]


# ============================================================


# Approach 5: Brute-Force Nested Loops
#
# Time Complexity: O(n * m)
# Auxiliary Space Complexity: O(1)
# Result Space: O(r)
#
# Every list1 word ni every list2 word tho compare chestunnam.

class Solution5:
    def findRestaurant(
        self,
        list1: List[str],
        list2: List[str]
    ) -> List[str]:

        minimum_sum = float("inf")
        result = []

        for first_index, first_word in enumerate(list1):
            for second_index, second_word in enumerate(list2):
                if first_word != second_word:
                    continue

                current_sum = first_index + second_index

                if current_sum < minimum_sum:
                    minimum_sum = current_sum
                    result = [first_word]

                elif current_sum == minimum_sum:
                    result.append(first_word)

        return result
