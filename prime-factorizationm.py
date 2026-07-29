n = int(input("Enter a number: "))
PRIMEFACTORS = []
for i in range(1, n+1):
    if n%i == 0:
        count = 0
        for _ in range(1, i):
            if i%_ == 0:
                count += 1
            if count == 1:
                while (n%i == 0):
                    PRIMEFACTORS.append(i)
                    n = n/i
print("Prime factors of", n, "are:", PRIMEFACTORS)