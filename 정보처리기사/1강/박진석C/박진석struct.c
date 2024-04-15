// 구조체
#include <stdio.h> // Standard input and Output Library 의약자로 입/출력을 실행하기위한 헤더
#include <string.h>
// 데이터(변수)를 체계적으로 관리하기 위한 문법 (관련 정보를 하나의 의미로 묶을 때 사용)
// - 자바 Class와 유사
// - 배열과 달리 서로 가른 자료형 묶음 가능
struct PERSON {          
    char name[50];
    int age;
};

int main() {
    struct PERSON p1 = {"박진석", 29}; 
    struct PERSON p2;
    strcpy(p2.name, "박보리");
    int myMoney = 2481050;
    int kakaoSubs = 990;  
    int MonthlyRent = 500000 ;
    int annuityInsurance = 100000 ;
    int IRP = 100000 ;
    int subscription= 100000 ;
    int LeapAccount= 700000 ;
    int tel= 57000 ;
    int actualCostInsurance = 10100 ;
    int cesco = 19000 ;
    int transportationExpenses = 62000 ;
    int netflix= 13500 ;
    int Udok= 9900 ;
    int card = 600000;
    int bori = 20000;
    p2.age = 4;
    struct PERSON p3[2] = {
        {"손성우",30},
        {"전영후",25}
    };
    printf("이름:%s 나이:%d\n", p1.name, p1.age);
    printf("이름:%s 나이:%d\n", p2.name, p2.age);
    printf("이름:%s 나이:%d\n", p3[0].name, p3[0].age);
    printf("이름:%s 나이:%d\n", p3[1].name, p3[1].age);
    printf("남는돈 : %d 원 \n", myMoney - (kakaoSubs + MonthlyRent + annuityInsurance + IRP + subscription + LeapAccount + tel + actualCostInsurance + cesco+ transportationExpenses + netflix+ Udok + card + bori));
}