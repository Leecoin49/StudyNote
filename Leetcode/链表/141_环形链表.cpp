
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        //龟兔从同一起点出发。
        ListNode *slow = head;
        ListNode *fast = head;

        while(fast && fast -> next){
            slow = slow -> next;            //乌龟走一步
            fast = fast -> next -> next;    //兔子走两步
            if(fast == slow){               //相遇
                return true;
            }
        }
        return false;
    }
};