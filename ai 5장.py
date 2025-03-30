Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
list_ex= [10, 20, 30, 40, 50, 60, 70]
high = 5
low = 3
list_ex[low]
40
list_ex[low + 2]
60
list_ex[high-low]
30
list_ex[low-high]
60
list_ex[-1]
70
list_ex[-low]
50
list_ex[2 * 3]
70
list_ex[2] * 3
90
list_ex[5 % 4]
20
len(list_ex)
7
list1 = [3, 5, 7]
list2 = [2, 3, 4, 6]
for i in list1:
    for j in list2:
        print(f"{i} * {j} = {i * j}")

        
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 6 = 18
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 6 = 30
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 6 = 42
list1 = ['I like', 'I love']
list2 = ['pancakes.', 'kiwi juice.', 'espresso.']
SyntaxError: multiple statements found while compiling a single statement
list1 = ['I like', 'I love']
list2 = ['pancakes.','kiwi juice.', 'espresso.']
for phrase in list1:
    for food in list2:
        print(phrase, food)

        
I like pancakes.
I like kiwi juice.
I like espresso.
I love pancakes.
I love kiwi juice.
I love espresso.
n_list = [10, 20, 30, 50, 60]
total = 0
for num in n_list:
    total += num
print("리스트 원소들:", n_list)
SyntaxError: invalid syntax
n_list = [10, 20, 30, 50, 60]
total = 0
for num in n_list:
    total += num
    
SyntaxError: multiple statements found while compiling a single statement
n_list = [10, 20, 30, 50, 60]
total = 0
for num in n_list:
    total += num
    
SyntaxError: multiple statements found while compiling a single statement
n_list = [10, 20, 30, 50, 60]
total = 0
for num in n_list:
    total += num
    print("리스트 원소들 :", n_list)
    print("리스트 원소들의 합 :", total)

    
리스트 원소들 : [10, 20, 30, 50, 60]
리스트 원소들의 합 : 10
리스트 원소들 : [10, 20, 30, 50, 60]
리스트 원소들의 합 : 30
리스트 원소들 : [10, 20, 30, 50, 60]
리스트 원소들의 합 : 60
리스트 원소들 : [10, 20, 30, 50, 60]
리스트 원소들의 합 : 110
리스트 원소들 : [10, 20, 30, 50, 60]
리스트 원소들의 합 : 170
n_list = [10, 20, 30, 50, 60]
max_value = n_list[0]
for num in n_list:
    if num > max_value:
        max_value = num
        print("리스트 원소들 :", n_list)
        print("리스트 원소들 중 최댓값:", max_value)

        
리스트 원소들 : [10, 20, 30, 50, 60]
리스트 원소들 중 최댓값: 20
리스트 원소들 : [10, 20, 30, 50, 60]
리스트 원소들 중 최댓값: 30
리스트 원소들 : [10, 20, 30, 50, 60]
리스트 원소들 중 최댓값: 50
리스트 원소들 : [10, 20, 30, 50, 60]
리스트 원소들 중 최댓값: 60
numbers = list(map(int, input("5개의 수를 입력하세요: ").split()))
5개의 수를 입력하세요: 45 67 20 34 2
total = sum(numbers)
average = total/ len(numbers)
max_value = max(numbers)
min_value = min(numbers)
print("합 :", total)
합 : 168
print("평균 :", average)
평균 : 33.6
print("최댓값:", max_value)
최댓값: 67
print("최솟값:", min_value)
최솟값: 2
import math
n = int(input("n을 입력하세요: "))
n을 입력하세요: 10
numbers = list(map(float, input(f"{n}개의 수를 입력하세요: ").split()))
10개의 수를 입력하세요: 45 67 20 34 2 100 23 45 67 89
total = sum(numbers)
mean = total / n
variance = sum((x - mean) ** 2 for x in numbers) / n
std_dev = math.sqrt(variance)
print("합 :", total)
합 : 492.0
print("평균 :", mean)
평균 : 49.2
print("표준편차 :", round(std_dev, 2))
표준편차 : 29.72
greet = 'Have a beautiful day.'
print(greet[0:4])
Have
print(greet[7:16])
beautiful
print(greet[17:20])
day
animals = ['dog', 'cat', 'tiger', 'lion']
print("animals =", animals)
animals = ['dog', 'cat', 'tiger', 'lion']
animals.append(animals.pop(0))
print("animals =
      
SyntaxError: unterminated string literal (detected at line 1)
animals.append(animals.pop(0))
      
print("animals =", animals)
      
animals = ['tiger', 'lion', 'dog', 'cat']
animals = ['dog', 'cat', 'tiger', 'lion']
      
print("animals =", animals)
      
animals = ['dog', 'cat', 'tiger', 'lion']
for animals in animals:
      print("I love", animal + ".")

      
Traceback (most recent call last):
  File "<pyshell#82>", line 2, in <module>
    print("I love", animal + ".")
NameError: name 'animal' is not defined. Did you mean: 'animals'?
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc','opq', 'opq']
      
new_s_list = []
      
for item in s_list:
      if them not in new_s_list:
      new_s_list.append(item)
      
SyntaxError: expected an indented block after 'if' statement on line 2
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc','opq', 'opq']
      
new_s_list = []
      
for item in s_list:
      if them not in new_s_list:
      
SyntaxError: multiple statements found while compiling a single statement
>>> src = 'a2b3c6a2c3f1g1'
... output = ''
... i = 0
...       
SyntaxError: multiple statements found while compiling a single statement
>>> src= 'a2b3c6a2c3f1g1'
...       
>>> output = ''
...       
>>> i = 0
...       
>>> while i < len(src):
...     char = src[i]
...     i += 1
...     num_str = ''
...     while i < len(src) and src [i].isdigit():
...         num_str += src[i]
...         i += 1
...         num = int(num_str) if num_str else 1
...         output += char * num
...         print("src =", src)
...         print("output =", output)
... 
...         
src = a2b3c6a2c3f1g1
output = aa
src = a2b3c6a2c3f1g1
output = aabbb
src = a2b3c6a2c3f1g1
output = aabbbcccccc
src = a2b3c6a2c3f1g1
output = aabbbccccccaa
src = a2b3c6a2c3f1g1
output = aabbbccccccaaccc
src = a2b3c6a2c3f1g1
output = aabbbccccccaacccf
src = a2b3c6a2c3f1g1
output = aabbbccccccaacccfg
