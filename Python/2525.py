a,b = map(int, input().split())
m = int(input())

if b+(m%60) > 60:
    if b == 60:
        b = 0
    else:
        b = m%60
else:
    