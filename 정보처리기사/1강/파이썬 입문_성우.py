# 1991년 귀도 반 로섬(Guido van Rossum)이라는 프로그래머에 의해 개발된 언어

# 특징
# 1.
# 파이썬은 컴파일 과정 없이 인터프리터(Interpreter, 해석기)가 소스 코드를 
#     한 줄씩 읽어 들여 곧바로 실행하는 스크립트 언어(Script language)라서 
#     컴파일 과정이 필요하지 않아 실행 결과를 바로 확인하고 수정하면서 손쉽게 코드를 작성할 수 있다.

# 2.
# 파이썬은 동적 타입 언어이다. 변수의 자료형을 지정하지 않고 단순히 선언하는 것만으로도 값을 지정할 수 있다.

# 3.
# 플랫폼 독립적 Platform Independent 이다. 파이썬은 운영체제별로 컴파일 할 필요가 없기 때문에 
#     한번 소스 코드를 작성하면 어떤 운영체제에서든 활용이 가능하다.


# ※컴파일 언어와 스크립트 언어의 차이점
#     컴파일 언어는 ‘컴파일’이라는 과정을 통해 프로그래머(인간)이 작성한 코드를 기계어로 번역해 
#     실행하는 언어이다. 반면 스크립트 언어는 별도의 ‘컴파일’ 과정 없이 인터프리터가 소스 코드를 
#     한 줄씩 읽어가며 바로 실행하는 언어를 의미한다. 컴파일 언어는 소스 코드를 컴파일하는 과정을 
#     거쳐야 하므로 실행 및 수정에 비교적 많은 시간을 소요하지만, 한 번 기계어로 번역되면 
#     빠른 실행 속도를 보여준다. 스크립트 언어는 컴파일 없이 곧바로 실행하므로 결과를 바로 
#     확인하고 빠르게 수정할 수 있지만, 번역과 실행이 동시에 이뤄져 컴파일 언어보다 느린 실행 속도를 보인다.


# ---------------------------------------------------------------------------------

# 파이썬의 장점
# 쉽고 간결한 문법 : 파이썬은 읽기 쉽고 간결한 문법이라 학습이 쉽다.
# 동적 타이핑 : 변수를 명시적으로 선언하지 않아도 되며, 동적 타이핑으로 코드 작성이 편리하다.
# 다양한 라이브러리와 프레임워크 : 웹 개발, 데이터 분석, 인공지능, 기계학습 등 다양한 분야에서 활용이 가능하다.
# 커뮤니티 지원 : 활발한 커뮤니티와 개발자 생태계가 있어서 문제 해결이나 지원이 용이하다.
# 빠른 개발속도, 높은 확장성 및 이식성도 장점이다.


# 단점
# 성능 : 일부 언어에 비해 실행속도가 느릴 수 있다. 특히 CPU집약적인 작업에는 적합하지 않다.
# GIL Global Interpreter Look : CPython 구현에서 GIL 로 인해 멀티스레딩 성능이 제한될 수 있다.

# ---------------------------------------------------------------------------------


# 파이썬 활용사례

# Google(구글),
#     Google(구글)은 백엔드에 C++과 파이썬을 결합해 활용한다. 짧은 대기 시간과 엄격한 메모리 제어가 중요한 스택에는 
#     C++로 코드를 작성하고, 프로그램의 빠른 전달과 유지 관리가 필요한 부분에는 파이썬을 활용해 코드를 작성한다.

# Instagram(인스타그램),
#     Instagram은 파이썬으로 작성된 오픈 소스 웹 프레임워크 Django를 기본 서버 측 언어로 사용하고 있다.

# Netflix(넷플릭스),
#     Netflix는 방대한 표준 라이브러리, 간결하고 깔끔한 구문, 대규모 커뮤니티, 풍부한 타사 라이브러리 등을 이유로 
#     파이썬을 자사 서비스에 적극적으로 활용하고 있다.

# Spotify(스포티파이),
#     음악 스트리밍 및 미디어 서비스 제공 업체 Spotify의 앱은 Python을 활용해 빌드되었다. Spotify 엔지니어는 
#     Spotify 백엔드의 80%가 파이썬으로 작성되어 있다고 밝혔다고 한다.

# Dropbox(드롭박스),
#     클라우드에 사진, 문서, 등의 파일 보관 및 공유 서비스를 제공하는 플랫폼 Dropbox는 외부 오픈 소스 코드와 
#     자체 작성한 코드 모두에 파이썬을 사용하고 있다. Dropbox는 크로스 플랫폼 지원, 가독성, 학습 용이성 등 
#     파이썬이 지닌 장점 덕에 빠르게 서비스를 구현할 수 있었다고 한다. 파이썬의 창시자인 귀도 반 로썸은 
#     2012년부터 2019년까지 Dropbox에서 개발자로 재직하기도 했다.


# ---------------------------------------------------------------------------------
# [[[[[[[[[[실습 부문]]]]]]]]]]

print("Hello World");

# 파이썬을 사이트가서 다운받고, 돌아와서 "Ctrl + Shift + P" 
#  > Python: Run Python File inTerminal 를 하게되면 설치 안되어있다고 나오는데, 
#  이 때 경로 설정을 다운받은 곳으로하면 사용가능.
# "Ctrl + Shift + P" > Python: Run Python File inTerminal 을 선택하면 실행된다.
# 또는 Ctrl + F5를 눌러서 빠른실행 가능하다. (VSCode로 진행했음)

# 파이썬 주석은 샵 이다. Ctrl + / 를 하면 범위 주석 가능하다.

# 자동완성 기능 설정하기
# Visual Studio Code > File > Open File 
#  > 파일 열기화면에서 %APPDATA%\Code\User 을 주소창에 쓰고 settings.json 파일 열기 
#  > "python.languageServer": "Pylance" 추가

# ---------------------------------------------------------------------------------

# 변수

# 파이썬은 동적 타입(Dynamic Typing language) 로서, 변수를 선언할 때 명시적으로 타입을 지정할 필요가 없다. 
# 변수 타입은 변수에 할당되는 값에 따라서 자동으로 결정된다.
name = 'sori'
message = 'hi, '+name+' ... bye, '+name+'.'
print(message)

# ---------------------------------------------------------------------------------


# 숫자 데이터 타입
print(-1)
print(0)
print(1) #int
print(1.1) #float
print('1+1')
print('1+1', 1+1)
print('1-1', 1-1)
print('1*1', 1*1)
print('1/1', 1/1)


# math 는 다양한 수학 함수와 상수를 제공하는 표준 라이브러리 모듈 중 하나이다.
#  다양한 수학적 계산을 수행할 수 있게한다.
import math
print('print(math.pi)', print(math.pi)) #원주율 값 가져오기

print('math.sqrt(4)', math.sqrt(4)) #제곱근 계산 함수

angle_rad = math.radians(45) # 각도를 라디안으로 변환
print('math.sin(angle_rad)', math.sin(angle_rad))
print('math.cos(angle_rad)', math.cos(angle_rad))

print('math.sqrt(4,2)', math.pow(4,2)) #거듭제곱 계산함수

num = 10
print('math.log10(num)', math.log10(num)) #로그 계산 함수



import random
print('random.random()', random.random())

# ---------------------------------------------------------------------------------

# 문자 데이터 타입

print('Hello World')

print("Hello World")

print('''
    Hello 
    World
    ''')

print("'1'+'1'", '1'+'1')

print('Hello World'*1000) 

print("len('Hello World'*1000)", len('Hello World'*1000))

print("'Hello world'.replace('World', 'universe')", 'Hello world'.replace('World', 'universe'))

# ---------------------------------------------------------------------------------

# 리스트 데이터 타입

students = ["egoing", "sori", "maru"]

grades = [2, 1, 4]

print("students[1]", students[1])

print("len(students)", len(students))

print("min(grades)", min(grades))

print("max(grades)", max(grades))

print("sum(grades)", sum(grades))

import statistics #데이터의 표준 편차를 계산할 수 있다.(평균, 중간값, 표준편차, 분산 등)
print("statistics.mean(grades)", statistics.mean(grades)) #statistics.mean 은 평균을 구하는 함수

print("statistics.median(grades)", statistics.median(grades)) #statistics.median 은 중간값을 구하는 함수

print("statistics.stdev(grades)", statistics.stdev(grades)) #statistics.stdev 은 표준편차 구하는 함수
#표준편차 Standard Deviation 는 데이터의 산포도를 나타내는 통계적 측도로, 분산의 양의 제곱근으로 정의.

print("statistics.variance(grades)", statistics.variance(grades)) #statistics.variance 은 분산 구하는 함수
#분산은 활률 분포의 각 데이터가 평균에서 얼마나 떨어져있는지 나타내는 측도.

import random
print("random.choice(students)", random.choice(students)) #이렇게하면 아까 만든 문자열리스트중에 랜덤으로 값이 나온다.


# ---------------------------------------------------------------------------------
# 파이썬관련 문서를 보고 싶다면 파이썬 홈페이지 메뉴에 Documentation 을 참고
https://www.python.org/doc/
# ---------------------------------------------------------------------------------

