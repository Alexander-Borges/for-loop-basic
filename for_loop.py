for x in range(151):
    print(x)

for t in range(5,1001,5):
    print(t)

for v in range (1,101):
    if v % 10 == 0:
        print("Coding Dojo")
    elif v % 5 == 0:
        print("Coding")
    else:
        print(v)

sum = 0
for w in range(1,500001,2):
    sum += w
print(sum)

for k in range(2018,0,-4):
    print(k)

lowNum =2
highNum = 9
mult = 3
for r in range(lowNum, highNum+1):
    if r % mult == 0:
        print(r)