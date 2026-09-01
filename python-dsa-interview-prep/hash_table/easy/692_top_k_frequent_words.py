# LeetCode 692 - Top K Frequent Words
# Difficulty: Medium

# Recommended Current-Level Approach: HashMap + Sorting
# Recommended When k Is Small: HashMap + Heap Selection

# n = total number of words
# u = number of unique words
# k = number of words to return
#
# Below complexities use the usual simplified model:
# word hashing/comparison is treated as O(1).
# A string-length-aware explanation is provided below.


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Frequency HashMap + Sorting
# Your Approach
# Recommended Current-Level Approach
# Time Complexity: O(n + u log u)
# Space Complexity: O(u)
#
# Time Explanation:
# Frequencies build cheyadaniki O(n).
# u unique words ni sort cheyadaniki O(u log u).
# First k words slice cheyadaniki O(k).
# Total O(n + u log u), because k <= u.
#
# Space Explanation:
# Frequency dictionary and sorted keys kosam O(u).
# Returned slice kosam O(k).
# Total O(u).
#
# Sorting Rules:
# -frequency[word] → Higher frequency first.
# word             → Equal frequency ayite alphabetical order.
class Solution1:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = {}

        for word in words:
            frequency[word] = frequency.get(word, 0) + 1

        sorted_words = sorted(
            frequency,
            key=lambda word: (-frequency[word], word)
        )

        return sorted_words[:k]


# ============================================================


# Approach 2: HashMap + heapq.nsmallest()
# Useful When k Is Small Compared With u
# Time Complexity: O(n + u log(k + 1))
# Space Complexity: O(u)
#
# Time Explanation:
# Frequencies build cheyadaniki O(n).
# Required ordering key prakaram best k words select chestunnam.
# Heap-based selection kosam O(u log(k + 1)).
#
# Space Explanation:
# Frequency dictionary kosam O(u).
# Heap selection and result kosam O(k).
# Total O(u), because k <= u.
#
# Why nsmallest?
# Frequency ni negative chestunnam kabatti:
#
# Frequency 5 → -5
# Frequency 2 → -2
#
# -5 smaller kabatti frequency 5 word first select avutundi.
# Equal frequencies ayite alphabetical order follow avutundi.
class Solution2:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import heapq

        frequency = {}

        for word in words:
            frequency[word] = frequency.get(word, 0) + 1

        return heapq.nsmallest(
            k,
            frequency,
            key=lambda word: (-frequency[word], word)
        )


# ============================================================


# Approach 3: Build Heap + Pop k Words
# Time Complexity: O(n + u + k log(u + 1))
# Space Complexity: O(u)
#
# Time Explanation:
# Frequencies build cheyadaniki O(n).
# u entries tho heap create cheyadaniki heapify() O(u).
# k words pop cheyadaniki O(k log(u + 1)).
#
# Space Explanation:
# Frequency dictionary and heap kosam O(u).
# Result kosam O(k).
# Total O(u).
#
# Heap Entry:
# (-frequency, word)
#
# Heap first negative frequency ni compare chestundi.
# Tie ayite word alphabetical order ni compare chestundi.
class Solution3:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import heapq

        frequency = {}

        for word in words:
            frequency[word] = frequency.get(word, 0) + 1

        heap = [
            (-count, word)
            for word, count in frequency.items()
        ]

        heapq.heapify(heap)

        result = []

        for _ in range(k):
            negative_count, word = heapq.heappop(heap)
            result.append(word)

        return result


# ============================================================
# OTHER USEFUL SOLUTION
# ============================================================


# Approach 4: Frequency Buckets + Alphabetical Sorting
# Time Complexity: O(n + u log u)
# Space Complexity: O(n + u), simplified to O(n)
#
# Time Explanation:
# Frequencies build cheyadaniki O(n).
# n + 1 buckets create chestunnam.
# Same frequency unna words ni corresponding bucket lo store chestunnam.
# Prati visited bucket lo words alphabetical order lo sort chestunnam.
#
# Worst case lo anni unique words same bucket lo undavachu.
# Appudu alphabetical sorting O(u log u).
#
# Space Explanation:
# n + 1 buckets and frequency dictionary use chestunnam.
# Total O(n).
#
# Important:
# Top K Frequent Elements lo bucket sort linear time.
# Ee problem lo alphabetical tie-breaking kosam sorting kuda avasaram.
# Kabatti ee implementation guaranteed O(n) kaadu.
class Solution4:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = {}

        for word in words:
            frequency[word] = frequency.get(word, 0) + 1

        buckets = [[] for _ in range(len(words) + 1)]

        for word, count in frequency.items():
            buckets[count].append(word)

        result = []

        for count in range(len(words), 0, -1):
            for word in sorted(buckets[count]):
                result.append(word)

                if len(result) == k:
                    return result

        return result
