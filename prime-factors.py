n = int(input())
f = []
for i in range(2, n+1):
    while n % i == 0:
        f.append(i)
        n //= i
print("Prime factors are:", f)