'''
Armstrong number
'''
'''
n = int(input())
count = len(str(n))
s = 0
for digit in str(n):
    s += int(digit) ** count

print("Armstrong number" if s == n else "not an Armstrong number")
'''

'''Perfect Number'''
'''
n = int(input())
s = 0
for i in range(1,n//2+1):
    if n % i == 0:
        s += i

print("Perfect number" if s == n else "not a Perfect number")'''

'''Strong number'''

def factorial(n):
    if n < 0:
        return "no factorial for -ve"
    elif n ==  0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1,n+1):
            fact = fact *i
        return fact

n = int(input())
s = 0
for digit in str(n):
    s += factorial(int(digit))
print("Strong number" if s == n else "Not a Strong number")