#include <stdio.h>
#include <stdlib.h>
#include <math.h>

union val {
    int a;      //operand
    char b;     //operator
};

typedef struct node {
    int type;           //1=>operand, 2=>operator
    union val item;
    struct node *next;
} node;

int ISP(node *n) {
    if(n->type == 1) return 8;
    else {
        if(n->item->b == '+' || n->item->b == '-') return 2;
        else if(n->item->b == '*' || n->item->b == '/') return 4;
        else if(n->item->b == '^') return 5;
        else return 0;
    }
}

int ICP(node *n) {
    if(n->type == 1) return 7;
    else {
        if(n->item->b == '+' || n->item->b == '-') return 1;
        else if(n->item->b == '*' || n->item->b == '/') return 3;
        else if(n->item->b == '^') return 6;
        else if(n->item->b == '(') return 9;
        else return 0;
    }
}

node* convert(node *ptr) {
    node *top = NULL, *temp, *item, *out;
    out = (node*) malloc(sizeof(node));
    out->next = NULL;

    //push '('
    top = (node*) malloc(sizeof(node));
    top->type = 2;
    top->item->b = '('
    top->next = NULL;
    
    while(top!=NULL) {
        item = ptr;

        //pop()
        temp = top;
        top = top->next;
        temp->next = NULL;

        if(item->type == 1) {
            //push()
            temp->next = top;
            top = temp;

            out->next = item;
            out = out->next;
        }
        else if(item->item->b == ')') {
            while(temp->type == 2 && temp->item->b !='(') {
                out->next = temp;
                out = out->next;

                //pop()
                temp = top;
                top = top->next;
                temp->next = NULL;
            }
        }
        else if(ISP(temp)>=ICP(item)) {
            while(ISP(temp)>=ICP(item)) {
                out->next = temp;
                out = out->next;

                //pop()
                temp = top;
                top = top->next;
                temp->next = NULL;
            }
            //push()
            temp->next = top;
            top = temp;

            //push()
            item->next = top;
            top = item;
        }
        else if(ISP(temp)<ICP(item)) {
            //push()
            temp->next = top;
            top = temp;

            //push()
            item->next = top;
            top = item;
        }
    }
    return out;
}

int val(int a, char op, int b) {
    switch (op)
    {
    case '+':
        return a+b;
    case '-':
        return a-b;
    case '*':
        return a*b;
    case '/':
        return a/b;
    case '^':
        return (int) pow(a,b);
    default:
        return 0;
    }
}

void eval(node* ptr) {
    node *item = ptr, *top = NULL, *temp;
    char op;
    int a, b;
    item->next = NULL;
    ptr = ptr->next;
    while(item!=NULL) {
        if(item->type == 1) {
            item->next = top;
            top = item;
        }
        else {
            op = *(item->item);
            free(item);
            b = *(top->item);
            temp = top;
            top = top->next;
            free(temp);
            a = *(top->item);
            top->item = val(a,op,b);
        }
        item->next = NULL;
        ptr = ptr->next;
    }
    printf("Result: %d", *(top->item))
}

void main() {
    char c;
    node *lst = NULL, *temp, *ptr, *stk = NULL;
    printf("Enter the Infix expression: ");
    do {
        scanf("%c",&c);
        if(c!='\n') {
            temp = (node*) malloc(sizeof(node));
            if(c=='+' || c=='-' || c=='*' || c=='/' || c=='^' || c=='(' || c==')') {
                temp->type = 2;
                temp->item->b = c;
            }
            else {
                if(ptr->type == 1) {
                    ptr->item->a *= 10;
                    ptr->item->a += (c + '0');
                    free(temp);
                }
                else {
                    temp->type = 1;
                    temp->item->a = c+'0';
                    ptr->next = temp;
                    ptr = ptr->next;
                }
            }
            temp->next = NULL;
            if(lst = NULL) {
                lst = temp;
                ptr = lst;
            }
            else {
                ptr->next = temp;
                ptr = ptr->next;
            }
        }
    } while(c!='\n');
    temp = (node*) malloc(sizeof(node));
    temp->type = 2;
    temp->item = ')';
    temp->next = NULL;
    ptr->next = temp;

    ptr = convert(lst);

    eval(ptr);
}