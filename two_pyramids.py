n = int(input())
for _ in range(1, n+1):
    print(" "*(n-_)+ "*"*(2*_ - 1) + " "*(2*(n-_)) + "*"*(2*_ - 1))
    