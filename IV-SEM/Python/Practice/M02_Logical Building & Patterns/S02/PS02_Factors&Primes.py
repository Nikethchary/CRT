'''
n = int(input("Enter a number: "))
for i in range(1, n//2 + 1):
    if n % i == 0:
        print(i,end = " ")
print(n)
'''
'''
n = int(input())
counter = 0
for i in range(1, n//2+1):
    if n % i == 0:
        counter += 1
print(counter+1)
'''
'''
n = int(input())
counter = 0
for i in range(2, n//2+1):
    if n % i == 0:
        counter += 1
print("prime" if counter == 0 else "not prime")
'''
'''
start = int(input())
end = int(input())
if start == 1:
    start = 2
for n in range(start, end+1):
    if n % i == 0:
        counter = 0
        for i in range(2,n//2+1):
            if n % i == 0:
                counter += 1
        if counter == 0:
            print(n,end=" ")'''
'''
n = int(input())
if n < 0:
    print("no factorial for -ve")
elif n ==0 or n == 1:
    print(1)
else:
    fact = 1
    for i in range(2,n+1):
        fact *= i
    print(fact)'''
'''GCD OF TWO NUMBERS'''
a = int(input())
b = int(input())
while b:
    a,b = b, a % b
print(a)

import math
print(math.gcd(a,b))
