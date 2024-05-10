struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

/*
    这个代码是用于找到两个链表的交点的解决方案。给出两个链表的头指针 `headA` 和 `headB`，目标是找到它们的交点节点。如果两个链表没有交点，返回 `nullptr`。

    **代码结构**：
    - `ListNode` 结构体定义了链表节点，有一个整数值 `val` 和一个指向下一个节点的指针 `next`。
    - `Solution` 类中的 `getIntersectionNode` 方法用于找到两个链表的交点。

    **逻辑**：
    1. **创建指针**：
    - 创建两个指针 `A` 和 `B`，分别指向两个链表的头部。

    2. **遍历链表**：
    - 通过 `while (A != B)` 循环，继续迭代，直到 `A` 和 `B` 相遇。
    - 每一步中，指针 `A` 指向它当前节点的下一个节点，如果 `A` 为 `nullptr`，则跳到 `headB`。
    - 同样地，指针 `B` 指向它当前节点的下一个节点，如果 `B` 为 `nullptr`，则跳到 `headA`。

    3. **遇到交点或到达末尾**：
    - 通过这样的方式，指针 `A` 和 `B` 最终会在交点相遇，或者同时到达末尾（即 `nullptr`）。
    - 如果链表相交，指针 `A` 和 `B` 会在交点处相遇，因为它们循环遍历了两个链表的长度。
    - 如果链表不相交，指针 `A` 和 `B` 会同时到达 `nullptr`，此时返回 `nullptr`，表示没有交点。

    这个方法的关键在于让两个指针遍历相同的节点数量，以确保找到交点或确认没有交点。由于两个指针最终会遍历相同的路径长度，无论链表的实际长度如何，这种方法保证了在有限步骤内找到交点。
*/

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *A = headA, *B = headB;
        while (A != B) {
            A = A != nullptr ? A->next : headB;
            B = B != nullptr ? B->next : headA;
        }
        return A;
    }
};