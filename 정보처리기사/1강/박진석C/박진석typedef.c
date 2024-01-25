// unsigned int temp; # 이렇게 쓰면 번거로우므로
// typedef unsigned int PJS; # PJS 로 정의
// PJS temp;

#include <stdio.h>
// 구조체의 경우 다음과 같이 정의 할수있다
typedef struct {
    char name[200];
    int age;
    char address[100];
} PERSON;

int main() {
    PERSON p4 = {"박진석",29,"서울"};
    printf(" 이름 : %s  나이 : %d  사는곳 : %s", p4.name, p4.age, p4.address);
};