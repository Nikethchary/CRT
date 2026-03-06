'''li1 = ['a','b','c']
res = ""
for ch in li1:
    res += ch
print(res)
print("".join(li1))'''

'''Intermediate patterns'''
'''
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i) + "* "*i)
'''
'''
n = int(input())
for i in range(n,0,-1):
    print(" "*(n-i) + "* "*i)
'''
'''
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i) + "* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i) + "* "*i)
'''
'''
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i) + " ".join(str(j) for j in range(1,i+1)))

for i in range(1,n+1):
    print(" "*(n-i) + " ".join(str(j) for j in range(1,i+1)))
'''

n = int(input())
val = 65
for i in range(n):
    for j in range(i+1):
        print(chr(val),end=" ")
        val += 1
    print()