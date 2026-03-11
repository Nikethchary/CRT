'''nums = [1,2,3,4]
res = []
s = 0
for ele in nums:
    s += ele
    res.append(s)
print(res)'''

'''t = (1,2,3,45,50)
t2 = (2,3,547,8)
print(t,t2)

t = (1,2,3,45,50)
print(t[1:])
print(t[0:3])

t = (1,2,3,45,50)
del t
print(t)'''

d = {"name":"Niketh", "age":20}
print(d.get('name'))
print(d.keys())
print(d.values())

d = {"name":"Niketh", "age":20}
d['phn'] = 1234567890
print(d)
d['name'] = "Niketh chary"
print(d)

d = {"name":"Niketh", "age":20}
del d['age']
print(d.popitem())
d.clear()
print(d)