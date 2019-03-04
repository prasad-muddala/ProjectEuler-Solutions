t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a,b,sum = 0,2,0
    while (b<=n):
        sum += b
        a,b = b, a+4*b
    print(sum)
    
