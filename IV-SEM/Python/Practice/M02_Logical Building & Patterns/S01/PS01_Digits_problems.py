'''
n = int(input())
count = 0
while n > 0:
    count += 1
    n = n // 10
print(count)
'''
'''
n = int(input())
temp = n
s = 0
while n > 0:
    s += n % 10
    n = n // 10
print(s)
print(sum(map(int,str(temp))))
'''
'''
n = int(input())
even = odd = 0
while n > 0:
    d = n % 10
    if (d % 2) == 0:
        even += 1
    else:
        odd += 1
    n = n // 10
print(even, odd)
'''
n = int(input())
while n > 9:
    n = sum(map(int, str(n)))
print(n)