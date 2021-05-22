#include<stdio.h>
#include<stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
 };


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* temp1 = l1;
    struct ListNode* temp2 = l2;
    
    
    struct ListNode* resList = NULL;
    struct ListNode* temp3 = NULL;
    
    int carry = 0;
    while(temp1 != NULL || temp2 != NULL){
        
        struct ListNode* newNode = (struct ListNode *)malloc(sizeof(struct ListNode));
        
        int res;
        if(temp1 == NULL){
            
            res = temp2->val;
            temp2 = temp2->next;
            
        } else if (temp2 == NULL){
            
            res = temp1->val;
            temp1 = temp1->next;
            
        } else {
            
            res = temp1->val + temp2->val;
            temp1 = temp1->next;
            temp2 = temp2->next;
            
        }
        
        res += carry;
        if(res >= 10){
            res = res%10;
            carry = 1;
        } else {
            carry = 0;
        }
        
        newNode->val = res;
        newNode->next = NULL;
        
        if(resList == NULL){
            resList = newNode;
            temp3 = newNode;
        } else {
            temp3->next = newNode;
            temp3 = temp3->next;
        }
    }
    if(carry == 1){
        struct ListNode* newNode = (struct ListNode *)malloc(sizeof(struct ListNode));
        newNode->val = 1;
        newNode->next = NULL;
        temp3->next = newNode;
        temp3 = temp3->next;
    }
    return resList;
}
int main(){

    int a,b;
    printf("Enter two Numbers:: ");
    scanf("%d%d",&a,&b);

    struct ListNode* l1 = NULL;
    struct ListNode* l2 = NULL;

    struct ListNode* temp1 = NULL;
    struct ListNode* temp2 = NULL;

    while(a != 0){
        struct ListNode* newNode = (struct ListNode *)malloc(sizeof(struct ListNode));

        newNode->val = a%10;
        newNode->next = NULL;

        a /= 10;

        if(l1 == NULL){
            l1 = newNode;
            temp1 = l1;
        } else {
            temp1->next = newNode;
            temp1 = temp1->next;
        }
    }

    while(b != 0){
        struct ListNode* newNode = (struct ListNode *)malloc(sizeof(struct ListNode));

        newNode->val = b%10;
        newNode->next = NULL;

        b /= 10;

        if(l2 == NULL){
            l2 = newNode;
            temp2 = l2;
        } else {
            temp2->next = newNode;
            temp2 = temp2->next;
        }
    }

    struct ListNode* resList = addTwoNumbers(l1,l2);
    
    while(resList != NULL){
        printf("%d",resList->val);
        resList = resList->next;
    }
    printf("\n");

    return 0;
}