n = int(input())
for i in range(n//2, n+1, 2):
    print(" "*(n-i-1) + "*"*i + " "*(n-i) + "*"*i)
for i in range(n, 0, -1):
    print(" "*(n-i) + "*"*(2*i-1))