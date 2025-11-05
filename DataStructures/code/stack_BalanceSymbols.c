#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAX 100

//数据准备
typedef struct Stack {
	int top;
	char str[MAX];
}Stack;

//初始化栈
void init(Stack* s) {
	s->top = -1;
}

//判断栈是否为空
int isEmpty(Stack* s) {
	if (s->top == -1) {
		//printf("栈为空");
		return 1;
	}
	return 0;
}

//入栈
void push(Stack* s,char x) {
	s->str[++s->top] = x;
}

//出栈
void pop(Stack* s, char* x) {
	*x = s->str[s->top--];
}

//读取栈顶元素
char getTop(Stack* s) {
	if (isEmpty(s))	return 0;
	return s->str[s->top];
}

//匹配函数
int isMatch(char left, char right) {
	return (left == '(' && right == ')') ||
		(left == '[' && right == ']') ||
		(left == '{' && right == '}');
}

int main() {
	Stack* s = (Stack*)malloc(sizeof(Stack));
	init(s);
	char a[100];
	char b[6] = { '(','[','{',')',']','}' };
	scanf("%s", a);
	char c;
	for (int i = 0;i < strlen(a);i++) {
		c = a[i];
		if (c == b[0] || c == b[1] || c == b[2]) {
			push(s, c);
		}
		char v = getTop(s);
		if (c == b[3] || c == b[4] || c == b[5]) {
			if (isMatch(v, c)) {
				char t;
				pop(s, &t);
			}
			else
			{
				printf("不匹配\n");
				break;
			}
		}
	}
	if (isEmpty(s)) {
		printf("匹配\n");
	}
	else
	{
		printf("不匹配\n");
	}

	return 0;
}