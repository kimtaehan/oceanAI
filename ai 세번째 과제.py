Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print(100, '+', 200, '=', 100 + 200)
100 + 200 = 300
print(200, '+', 300, '+', 400, '=', 200 + 300 + 400)
200 + 300 + 400 = 900
width = 30
height = 60
print(width)
30
print(height)
60
# get_rect_area.py

width = 30
height = 60
area = width * height

print("사각형의 면적:", area)

SyntaxError: multiple statements found while compiling a single statement
width = 30
height = 60
area = width * height
print("사각형의 면적:", area)
사각형의 면적: 1800
width = 40
height = 20
area = (width * height)/2
print("삼각형의 면적:", int(area))
삼각형의 면적: 400
side = int(input("정사각형의 밑변을 입력하세요:"))
정사각형의 밑변을 입력하세요:
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    side = int(input("정사각형의 밑변을 입력하세요:"))
ValueError: invalid literal for int() with base 10: ''
side = int(input("정사각형의 밑변을 입력하세요:"))
정사각형의 밑변을 입력하세요:40
area = side * side
print("정사각형의 밑변:",side)
정사각형의 밑변: 40
print("정사각형의 면적:", area)
정사각형의 면적: 1600
sum_value = sum(range(10,11))
print("10에서 10까지의 합:", sum_value)
10에서 10까지의 합: 10
sum_value = sum(range(10,15))
print("10에서 14까지의 합:", sum_value)
10에서 14까지의 합: 60
result = 101 * 101 * 101 * 101
print("101=", result)
101= 104060401
result = 101 ** 4
print("101 =", result)
101 = 104060401
for i in range(1, n+1):
    print(i, i ** 2)
n=6
SyntaxError: invalid syntax
n=6
for i in range(1, n+1):
    print(i, i ** 2)

    
1 1
2 4
3 9
4 16
5 25
6 36

def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius + 32

print("섭씨\t화씨")
for celsius in range(0, 51, 10):
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}\t{fahrenheit:.1f}")

SyntaxError: invalid syntax
def celsius_to_fahrenheit(celsius):
    return (9/5) *  celsius + 32

print("섭씨\t화씨")
섭씨	화씨
for celsius in range(0,51,10):
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"(celsius)\t(fahrenheit:.1f)")

    
(celsius)	(fahrenheit:.1f)
(celsius)	(fahrenheit:.1f)
(celsius)	(fahrenheit:.1f)
(celsius)	(fahrenheit:.1f)
(celsius)	(fahrenheit:.1f)
(celsius)	(fahrenheit:.1f)
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)

... fahrenheit = float(input("화씨 온도를 입력하세요: "))
... celsius = fahrenheit_to_celsius(fahrenheit)
... print(f"화씨 {fahrenheit} 도는 섭씨 {celsius:.1f} 도 입니다.")
... 
SyntaxError: invalid syntax
>>> def fahrenheit_to_celsius(fahrenheit):
...     return (fahrenheit - 32) * (5/9)
... 
... fahrenheit = float(input("화씨 온도를 입력하세요: "))
... celsius = fahrenheit_to_celsius(fahrenheit)
... print(f"화씨 {fahrenheit} 도는 섭씨 {celsius:.1f} 도 입니다.")
SyntaxError: invalid syntax
>>> def fahrenheit_to_celsius(fahrenheit):
...     return (fahrenheit - 32) * (5/9)
... 
>>> fahrenheit = float(input("화씨 온도를 입력하세요:"))
화씨 온도를 입력하세요:86
>>> celsius = fahrenheit_to_celsius(fahrenheit)
>>> print(f"화씨 (fahrenheit) 도는 섭씨 (celsius:.1f)도 입니다.")
화씨 (fahrenheit) 도는 섭씨 (celsius:.1f)도 입니다.
>>> import math
... 
... radius = 11
... PI = 3.141592
SyntaxError: multiple statements found while compiling a single statement
>>> import math
>>> radius = 11
>>> PT = 3.141592
>>> circumsference = 2* PT * radius
>>> area = PI * (radius ** 2)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    area = PI * (radius ** 2)
NameError: name 'PI' is not defined
>>> import math
... radius = 11
... PT = 3.141592
... circumsference = 2* PT * radius
SyntaxError: multiple statements found while compiling a single statement
