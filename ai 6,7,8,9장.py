Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from datetime import date
start_date = date(2019, 2, 14)
today = date.today()
delta = today - start_date
print(f"춘향이와 몽룡이의 연애 시작일 : {start_date.year}년 {start_date.month}월 {start_date.today}일")
춘향이와 몽룡이의 연애 시작일 : 2019년 2월 <built-in method today of type object at 0x00007FFF88B615B0>일
print(f"연애 시작일로부터 경과한 날짜 : {delta.days}일")
연애 시작일로부터 경과한 날짜 : 2250일
from datetime import date, timedelta
start_date = date(2019, 2, 14)
day_100 = start_date + timedelta(days=100)
day_200 = start_date + timedelta(days=200)
day_500 = start_date + timedelta(days=500)
days_1000 = start_date + timedelta(days=1000)
print(f"춘향이와 몽룡이의 연애 시작일: {start_date.year}년 {start_date.month}월 {start_date.day}일")
춘향이와 몽룡이의 연애 시작일: 2019년 2월 14일
print(f"100일 기념일: {day_100.year}년 {day.100.month}월 {day_100.day}일")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(f"200일 기념일: {day_200.year}년 {day.200.month}월 {day_200.day}일")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(f"500일 기념일: {day_500.year}년 {day_500.month}월 {day_500.day}일")
500일 기념일: 2020년 6월 28일
print(f"1000일 기념일: {day_1000.year}년 {day_1000.month}월 {day_1000.day}일")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(f"1000일 기념일: {day_1000.year}년 {day_1000.month}월 {day_1000.day}일")
NameError: name 'day_1000' is not defined. Did you mean: 'day_100'?
import math
for deg in range(0, 181, 10):
    rad = math.radians(deg)
    sin_val = math.sin(rad)
    cos_val = math.cos(rad)
    tan_val = math.tan(rad)
    print(f"sin({deg:3}) = {sin_val:6.3f}, cos({deg:3}) = {cos_val:6.3f}, tan({deg:3}) = tan_va;:3f})
          
SyntaxError: f-string: single '}' is not allowed
import math
for deg in range(0, 181, 10):
    rad = math.radians(deg)
    sin_val = math.sin(rad)
    cos_val = math.cos(rad)
    tan_val = math.tan(rad)
    print(f"sin({deg:3}) = {sin_val:6.3f}, cos({deg:3}) = {cos_val:6.3f}, tan({deg:3}) = {tan_val:3f}")
    
SyntaxError: multiple statements found while compiling a single statement
import random
target = random.randint(1, 20)
count = 0
while True:
    guess = int(input("1~20까지의 숫자를 입력하세요:"))
    count += 1
    if guess < target:
        print(f"{guess} 보다 큽니다!")
        elif guess > target:
            
SyntaxError: invalid syntax
import random

# 1~20 사이의 숫자 하나 생성
target = random.randint(1, 20)
count = 0  # 시도 횟수

while True:
    guess = int(input("1~20까지의 숫자를 입력하세요: "))
    count += 1

    if guess < target:
        print(f"{guess} 보다 큽니다!")
    elif guess > target:
        print(f"{guess} 보다 작습니다!")
    else:
        print("정답입니다!")
        if count <= 3:
            print(f"{count}번만에 맞춘 당신은 천재!")
        elif count <= 6:
            print(f"{count}번만에 맞추셨네요. 잘했어요^^")
        else:
            print(f"{count}번만에 맞추다니 쩝쩝...")
        break  # 정답 맞추면 반복 종료

SyntaxError: multiple statements found while compiling a single statement


... # 1~20 사이의 숫자 하나 생성
... target = random.randint(1, 20)
... count = 0  # 시도 횟수
... 
... while True:
...     guess = int(input("1~20까지의 숫자를 입력하세요: "))
...     count += 1
... 
...     if guess < target:
...         print(f"{guess} 보다 큽니다!")
...     elif guess > target:
...         print(f"{guess} 보다 작습니다!")
...     else:
...         print("정답입니다!")
...         if count <= 3:
...             print(f"{count}번만에 맞춘 당신은 천재!")
...         elif count <= 6:
...             print(f"{count}번만에 맞추셨네요. 잘했어요^^")
...         else:
...             print(f"{count}번만에 맞추다니 쩝쩝...")
...         break  # 정답 맞추면 반복 종료
...     
SyntaxError: multiple statements found while compiling a single statement
>>> a, b = input('두 수를 입력하시오 : ').split()
... result = int(a) * int(b)
SyntaxError: multiple statements found while compiling a single statement
