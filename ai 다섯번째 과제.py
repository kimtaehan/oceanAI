Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for i in range(1, 10):
    print(f"2 * {1} = {2 * I}")
i= 1
SyntaxError: invalid syntax
for i in range(1, 10):
    print(f"2 * {1} = {2 * I}")

    
Traceback (most recent call last):
  File "<pyshell#4>", line 2, in <module>
    print(f"2 * {1} = {2 * I}")
NameError: name 'I' is not defined
KeyboardInterrupt
for i in range(1, 10):
    print(f"2 * {i} = {2 * i}")

    
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
i = 1
while i < 10:
    print(f"2 * {i} = {2 * i}")
    i += 1

    
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
for i in range(3):
    print('Python ')
    print('is ')
    print('FUN! ')

    
Python 
is 
FUN! 
Python 
is 
FUN! 
Python 
is 
FUN! 
for i in range(3):
    print('Python ')
    print('is ')
print('FUN! ')
SyntaxError: invalid syntax
for i in range(3):
    print('Python ')
    print('is ')
 print('FUN! ')
 
SyntaxError: unindent does not match any outer indentation level
for i in range(3):
    print('Python ')
    print('is ')
 print('FUN! ')
 
SyntaxError: unindent does not match any outer indentation level
for i in range(3):
    print('Python ')
print('is ')
SyntaxError: invalid syntax
def menu_selection():
    menu = {
        "b": "햄버거",
        "c": "치킨",
        "c": "피자"
        }
    while True:
        print("/n맛나 식당에 오신 것을
              
SyntaxError: unterminated string literal (detected at line 8)
def menu_selection():
    menu = {
        "b": "햄버거",
        "c": "치킨",
        "c": "피자"
        }
    while True:
        print("/n맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
        print("햄버거(b)")
        print("치킨(c)")
        print("피자(p)")
        choice = input("메뉴를 선택하세요(알파벳 b,c,p 입력):").strip().lower(0
               if choice in menu:
                                                                 
SyntaxError: '(' was never closed
def menu_selection():
    menu = {
        "b": "햄버거",
        "c": "치킨",
        "c": "피자"
        }
    while True:
        print("/n맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
        print("햄버거(b)")
        print("치킨(c)")
        print("피자(p)")
        choice = input("메뉴를 선택하세요(알파벳 b,c,p 입력):").strip().lower()
               if choice in menu:
                   
SyntaxError: unexpected indent
def menu_selection():
    menu = {
        "b": "햄버거",
        "c": "치킨",
        "c": "피자"
        }
    while True:
        print("/n맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
        print("햄버거(b)")
        print("치킨(c)")
        print("피자(p)")
        choice = input("메뉴를 선택하세요(알파벳 b,c,p 입력):").strip().lower()
            if choice in menu:
                
SyntaxError: unexpected indent
def menu_selection():
    menu = {
        "b": "햄버거",
        "c": "치킨",
        "c": "피자"
        }
    while True:
        print("/n맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
        print("햄버거(b)")
        print("치킨(c)")
        print("피자(p)")
        choice = input("메뉴를 선택하세요(알파벳 b,c,p 입력):").strip().lower()
    if choice in menu:
        print(f"{menu[choice]}을(를) 선택하셨습니다.")
        break
    
SyntaxError: 'break' outside loop
def menu_selection():
    menu = {
        "b": "햄버거",
        "c": "치킨",
        "c": "피자"
        }
    while True:
        print("/n맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
        print("햄버거(b)")
        print("치킨(c)")
        print("피자(p)")
        choice = input("메뉴를 선택하세요(알파벳 b,c,p 입력):").strip().lower()
            if choice in menu:
                
SyntaxError: unexpected indent
def menu_selection():
    menu = {
        "b": "햄버거",
        "c": "치킨",
        "c": "피자"
        }
    while True:
        print("/n맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
        print("햄버거(b)")
        print("치킨(c)")
        print("피자(p)")
        choice = input("메뉴를 선택하세요(알파벳 b,c,p 입력):").strip().lower()
    if choice in menu:
        print(f"{menu[choice]}을(를) 선택하셨습니다.")
    break
SyntaxError: 'break' outside loop
def menu_selection():
    menu = {
        "b": "햄버거",
        "c": "치킨",
        "c": "피자"
        }
    while True:
        print("/n맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
        print("햄버거(b)")
        print("치킨(c)")
        print("피자(p)")
        choice = input("메뉴를 선택하세요(알파벳 b,c,p 입력):").strip().lower()
    if choice in menu:
        print(f"{menu[choice]}을(를) 선택하셨습니다.")
    else:
        print("잘못된 입력입니다. 다시 입력하세요.")
    menu_selection()

    


def menu_selection():
    menu = {
        "b": "햄버거",
        "c": "치킨",
        "c": "피자"
        }
    while True:
        print("/n맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
        print("햄버거(b)")
        print("치킨(c)")
        print("피자(p)")
        choice = input("메뉴를 선택하세요(알파벳 b,c,p 입력):").strip().lower()
    if choice in menu:
        print(f"{menu[choice]}을(를) 선택하셨습니다.")
    else:
        print("잘못된 입력입니다. 다시 입력하세요.")
    menu_selection()

    
def menu_selection():
    menu = {
        "b": "햄버거",
        "c": "치킨",
        "c": "피자"
        }
    while True:
        print("/n맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
        print("햄버거(b)")
        print("치킨(c)")
        print("피자(p)")
        choice = input("메뉴를 선택하세요(알파벳 b,c,p 입력):").strip().lower()
    if choice in menu:
        print(f"{menu[choice]}을(를) 선택하셨습니다.")                                    break
    else:
        print("잘못된 입력입니다. 다시 입력하세요.")
    menu_selection()
    
SyntaxError: invalid syntax
def menu_selection():
    menu = {
        "b": "햄버거",
        "c": "치킨",
        "c": "피자"
        }
    while True:
        print("/n맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
        print("햄버거(b)")
        print("치킨(c)")
        print("피자(p)")
        choice = input("메뉴를 선택하세요(알파벳 b,c,p 입력):").strip().lower()
    if choice in menu:
        print(f"{menu[choice]}을(를) 선택하셨습니다.")
        break
    
SyntaxError: 'break' outside loop
print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
print("- 햄버거(입력 b)")
print("- 치킨(입력 c)")
print("- 피자(입력 p)")

while True:
    choice = input("메뉴를 선택하세요(알파벳 b, c, p 입력) : ").lower()
    
    if choice == 'b':
        print("햄버거를 선택하였습니다.")
        break
    elif choice == 'c':
        print("치킨을 선택하였습니다.")
        break
    elif choice == 'p':
        print("피자를 선택하였습니다.")
        break
    else:
        print("메뉴를 다시 입력하세요(알파벳 b, c, p 입력) : ")
        
SyntaxError: multiple statements found while compiling a single statement
print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.") 
print("- 햄버거(입력 b)")
print("- 치킨(입력 c)")
print("- 피자(입력 p)")

while True:
    choice = input("메뉴를 선택하세요(알파벳 b, c, p 입력) : ").lower()
    
    if choice == 'b':
        print("햄버거를 선택하였습니다.")
        break
    elif choice == 'c':
        print("치킨을 선택하였습니다.")
        break
    elif choice == 'p':
        print("피자를 선택하였습니다.")
        break
    else:
        print("메뉴를 다시 입력하세요(알파벳 b, c, p 입력) : ")
        
SyntaxError: multiple statements found while compiling a single statement
def is_prime(n):
    """주어진 숫자가 소수인지 판별하는 함수"""
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:  # 2를 제외한 모든 짝수는 소수가 아님
        return False
    
    # 3부터 n의 제곱근까지 홀수로만 나누어 확인
    for i in range(3, int(n**0.5) + 1, 2):
...         if n % i == 0:
...             return False
...     return True
... 
... # 사용자 입력 받기
... n = int(input("숫자를 입력하세요 : "))
... 
... # 소수 판별 결과 출력
... if is_prime(n):
...     print(f"{n}는 소수입니다")
... else:
...     print(f"{n}는 소수가 아닙니다")
...     
SyntaxError: invalid syntax
>>> def is_prime(n):
...     """주어진 숫자가 소수인지 판별하는 함수"""
...     if n <= 1:
...         return False
...     elif n == 2:
...         return True
...     elif n % 2 == 0:  # 2를 제외한 모든 짝수는 소수가 아님
...         return False
...     
...     # 3부터 n의 제곱근까지 홀수로만 나누어 확인
...     for i in range(3, int(n**0.5) + 1, 2):
...         if n % i == 0:
...             return False
...     return True
... 
... # 사용자 입력 받기
... num = int(input("숫자를 입력하세요 : "))
... 
... # 소수 판별 결과 출력
... if is_prime(n):
...     print(f"{n}는 소수입니다")
... else:
...     print(f"{n}는 소수가 아닙니다")
...     
SyntaxError: invalid syntax
