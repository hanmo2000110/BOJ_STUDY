#include<cstdio>
char c;
int main() {
	while (~scanf(" %c", &c))printf("%c", (c+10)%26+65);
	return 0;
}