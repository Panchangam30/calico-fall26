T= int(input())

for i in range(T):
    b,l,e = map(int,input().split())
    x = 0
    l = l-b
    b = -b
    total = 0
    if b - (50-e) <= 0:
        total += 50-e
        x+=1
        while total <= l:
            total += 50
            x += 1 

print(x)
        