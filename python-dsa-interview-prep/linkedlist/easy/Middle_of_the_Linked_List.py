
# LeetCode 876 - Middle of the Linked List
# Difficulty: Easy
# Recommended Approach: Slow and Fast Pointers
# Recommended Current-Level Approach: Two-Pass Approach


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Two-Pass Approach
# Your Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Time Explanation:
# First traversal lo linked list length calculate chestunnam.
# Tarvata count // 2 use chesi middle index calculate chestunnam.
# Second traversal lo middle node ki reach avutunnam.
# Rendu traversals maximum O(n) time teesukuntayi.
# Kabatti time complexity O(n).
#
# Space Explanation:
# Current, temp, count ane variables maatrame use chestunnam.
# Additional data structure create cheyadam ledu.
# Kabatti space complexity O(1).

class Solution1:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        current = head
        count = 0

        while current is not None:
            count += 1
            current = current.next

        mid_value = count // 2

        temp = head

        for _ in range(mid_value):
            temp = temp.next

        return temp


# ============================================================


# Approach 2: Slow and Fast Pointers
# Recommended Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Time Explanation:
# Slow pointer okka step move avutundi.
# Fast pointer rendu steps move avutundi.
# Fast pointer end ki reach ayye time ki
# slow pointer middle node daggara untundi.
# Linked list ni only one time traverse chestunnam.
# Kabatti time complexity O(n).
#
# Space Explanation:
# Slow and fast ane two pointers maatrame use chestunnam.
# Additional data structure avasaram ledu.
# Kabatti space complexity O(1).

class Solution2:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


# ============================================================


# Approach 3: Recursive Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Time Explanation:
# Recursion use chesi linked list lo prati node ni traverse chestunnam.
# Recursive calls complete ayye time ki total length calculate chestunnam.
# Middle index identify chesi corresponding node return chestunnam.
# Kabatti time complexity O(n).
#
# Space Explanation:
# Prati node kosam recursive function call create avutundi.
# Recursion call stack lo O(n) space use avutundi.
# Kabatti space complexity O(n).

class Solution3:
    def middleNode(self, head: ListNode | None) -> ListNode | None:

        def get_length(node):
            if node is None:
                return 0

            return 1 + get_length(node.next)

        def find_middle(node, steps):
            if steps == 0:
                return node

            return find_middle(node.next, steps - 1)

        length = get_length(head)
        middle_index = length // 2

        return find_middle(head, middle_index)


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Array / List Storage
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Time Explanation:
# First linked list lo unna nodes anni array lo store chestunnam.
# Tarvata len(nodes) // 2 use chesi middle node access chestunnam.
# Array index access O(1).
# Kabatti overall time complexity O(n).
#
# Space Explanation:
# Linked list lo unna prati node reference ni array lo store chestunnam.
# Kabatti space complexity O(n).

class Solution4:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        nodes = []
        current = head

        while current:
            nodes.append(current)
            current = current.next

        return nodes[len(nodes) // 2]


# ============================================================
# COMPLEXITY COMPARISON
# ============================================================
#
# Approach                 Time       Space
# Two-Pass                 O(n)       O(1)
# Slow and Fast Pointers   O(n)       O(1)
# Recursive                O(n)       O(n)
# Array Storage            O(n)       O(n)
#
# ============================================================
# FINAL RECOMMENDATION
# ============================================================
#
# Your Approach: Two-Pass Approach
# Best Interview Approach: Slow and Fast Pointers
# Best Current-Level Approach: Two-Pass Approach
#
# Note:
# For an even-length linked list, LeetCode expects
# the second middle node.
# Both Two-Pass and Slow-Fast approaches return it.
