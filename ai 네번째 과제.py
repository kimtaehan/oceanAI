Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a, b = 1, 1
for i in range(101):
    temp = a + b
...     a = b
...     b = temp
...     print('{}th Fib. Number is
...           
SyntaxError: unterminated string literal (detected at line 5)
>>> a, b =1, 1
...           
>>> for i in range(101):
...     temo = a + b
...     a = b
...     b = temp
... 
...           
Traceback (most recent call last):
  File "<pyshell#11>", line 4, in <module>
    b = temp
NameError: name 'temp' is not defined. Did you mean: 'temo'?
>>> a, b = 1, 1
...           
>>> for i in range(101):
...     temp = a + b
...     a = b
...     b = temp
...     print(' {}th Fib. Number is {}'.format(i + 2, b))
... 
...           
 2th Fib. Number is 2
 3th Fib. Number is 3
 4th Fib. Number is 5
 5th Fib. Number is 8
 6th Fib. Number is 13
 7th Fib. Number is 21
 8th Fib. Number is 34
 9th Fib. Number is 55
 10th Fib. Number is 89
 11th Fib. Number is 144
 12th Fib. Number is 233
 13th Fib. Number is 377
 14th Fib. Number is 610
 15th Fib. Number is 987
 16th Fib. Number is 1597
 17th Fib. Number is 2584
 18th Fib. Number is 4181
 19th Fib. Number is 6765
 20th Fib. Number is 10946
 21th Fib. Number is 17711
 22th Fib. Number is 28657
 23th Fib. Number is 46368
 24th Fib. Number is 75025
 25th Fib. Number is 121393
 26th Fib. Number is 196418
 27th Fib. Number is 317811
 28th Fib. Number is 514229
 29th Fib. Number is 832040
 30th Fib. Number is 1346269
 31th Fib. Number is 2178309
 32th Fib. Number is 3524578
 33th Fib. Number is 5702887
 34th Fib. Number is 9227465
 35th Fib. Number is 14930352
 36th Fib. Number is 24157817
 37th Fib. Number is 39088169
 38th Fib. Number is 63245986
 39th Fib. Number is 102334155
 40th Fib. Number is 165580141
 41th Fib. Number is 267914296
 42th Fib. Number is 433494437
 43th Fib. Number is 701408733
 44th Fib. Number is 1134903170
 45th Fib. Number is 1836311903
 46th Fib. Number is 2971215073
 47th Fib. Number is 4807526976
 48th Fib. Number is 7778742049
 49th Fib. Number is 12586269025
 50th Fib. Number is 20365011074
 51th Fib. Number is 32951280099
 52th Fib. Number is 53316291173
 53th Fib. Number is 86267571272
 54th Fib. Number is 139583862445
 55th Fib. Number is 225851433717
 56th Fib. Number is 365435296162
 57th Fib. Number is 591286729879
 58th Fib. Number is 956722026041
 59th Fib. Number is 1548008755920
 60th Fib. Number is 2504730781961
 61th Fib. Number is 4052739537881
 62th Fib. Number is 6557470319842
 63th Fib. Number is 10610209857723
 64th Fib. Number is 17167680177565
 65th Fib. Number is 27777890035288
 66th Fib. Number is 44945570212853
 67th Fib. Number is 72723460248141
 68th Fib. Number is 117669030460994
 69th Fib. Number is 190392490709135
 70th Fib. Number is 308061521170129
 71th Fib. Number is 498454011879264
 72th Fib. Number is 806515533049393
 73th Fib. Number is 1304969544928657
 74th Fib. Number is 2111485077978050
 75th Fib. Number is 3416454622906707
 76th Fib. Number is 5527939700884757
 77th Fib. Number is 8944394323791464
 78th Fib. Number is 14472334024676221
 79th Fib. Number is 23416728348467685
 80th Fib. Number is 37889062373143906
 81th Fib. Number is 61305790721611591
 82th Fib. Number is 99194853094755497
 83th Fib. Number is 160500643816367088
 84th Fib. Number is 259695496911122585
 85th Fib. Number is 420196140727489673
 86th Fib. Number is 679891637638612258
 87th Fib. Number is 1100087778366101931
 88th Fib. Number is 1779979416004714189
 89th Fib. Number is 2880067194370816120
 90th Fib. Number is 4660046610375530309
 91th Fib. Number is 7540113804746346429
 92th Fib. Number is 12200160415121876738
 93th Fib. Number is 19740274219868223167
 94th Fib. Number is 31940434634990099905
 95th Fib. Number is 51680708854858323072
 96th Fib. Number is 83621143489848422977
 97th Fib. Number is 135301852344706746049
 98th Fib. Number is 218922995834555169026
 99th Fib. Number is 354224848179261915075
 100th Fib. Number is 573147844013817084101
 101th Fib. Number is 927372692193078999176
 102th Fib. Number is 1500520536206896083277
