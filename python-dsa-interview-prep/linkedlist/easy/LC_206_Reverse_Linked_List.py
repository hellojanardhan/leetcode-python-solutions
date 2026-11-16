
# LeetCode 206 - Reverse Linked List
# Difficulty: Easy
# Recommended Approach: Iterative Three Pointers
# Recommended Current-Level Approach: Iterative Three Pointers


# ============================================================
# TOP 3 SOLUTIONS
# ============================================================


# Approach 1: Iterative Three Pointers
# Your Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Time Explanation:
# Linked list lo prati node ni okkasari traverse chestunnam.
# Next node address ni next_node lo save chestunnam.
# Current node next pointer ni previous node ki point chestunnam.
# Tarvata prev mariyu current pointers ni move chestunnam.
# Prati node ni okkasari process chestunnam.
# Kabatti time complexity O(n).
#
# Space Explanation:
# prev, current, next_node ane three pointers maatrame use chestunnam.
# Additional data structure create cheyadam ledu.
# Kabatti space complexity O(1).

class Solution1:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev


# ============================================================


# Approach 2: Recursive Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Time Explanation:
# Recursion use chesi linked list lo last node varaku traverse chestunnam.
# Last node new head avutundi.
# Recursive calls return ayye time lo
# current node next pointer ni reverse chestunnam.
# Prati node ni okkasari process chestunnam.
# Kabatti time complexity O(n).
#
# Space Explanation:
# Prati node kosam recursive function call create avutundi.
# Recursion call stack lo O(n) space use avutundi.
# Kabatti space complexity O(n).

class Solution2:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head


# ============================================================


# Approach 3: Stack Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Time Explanation:
# First traversal lo linked list nodes anni stack lo store chestunnam.
# Tarvata stack nunchi nodes ni pop chestu
# next pointers ni reverse order lo connect chestunnam.
# Prati node ni okkasari push and pop chestunnam.
# Kabatti time complexity O(n).
#
# Space Explanation:
# Linked list lo unna prati node reference ni stack lo store chestunnam.
# Stack lo maximum n nodes untayi.
# Kabatti space complexity O(n).

class Solution3:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

        if head is None:
            return None

        stack = []

        current = head

        while current:
            stack.append(current)
            current = current.next

        new_head = stack.pop()
        current = new_head

        while stack:
            current.next = stack.pop()
            current = current.next

        current.next = None

        return new_head


# ============================================================
# OTHER POSSIBLE SOLUTIONS
# ============================================================


# Approach 4: Recursive Approach Using Helper Function
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Time Explanation:
# Recursive helper function use chesi nodes ni reverse chestunnam.
# Prati recursive call oka node ni process chestundi.
# Kabatti time complexity O(n).
#
# Space Explanation:
# Recursive calls kosam call stack use avutundi.
# Maximum n recursive calls untayi.
# Kabatti space complexity O(n).

class Solution4:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

        def reverse(previous, current):

            if current is None:
                return previous

            next_node = current.next
            current.next = previous

            return reverse(current, next_node)

        return reverse(None, head)


# ============================================================
# COMPLEXITY COMPARISON
# ============================================================
#
# Approach                  Time       Space
# Iterative Three Pointers  O(n)       O(1)
# Recursive                 O(n)       O(n)
# Stack                     O(n)       O(n)
# Recursive Helper          O(n)       O(n)
#
# ============================================================
# FINAL RECOMMENDATION
# ============================================================
#
# Your Approach: Iterative Three Pointers
# Best Interview Approach: Iterative Three Pointers
# Recommended Approach: Iterative Three Pointers
#
# Your solution is optimal in both time and space.
#
# Important:
# next_node = current.next
# Ee statement chala important.
# Pointer reverse cheyadaniki mundu next node address save cheyyali.
# Lekapothe remaining linked list connection lose avutundi.
