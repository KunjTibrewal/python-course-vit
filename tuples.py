a = (1, 2, 3, 4, 5)
b = (5, 7, 8, 9, 10)
c = a + b
print("Tuple a:", a)                                                           # (1, 2, 3, 4, 5)
print("Tuple b:", b)                                                           # (5, 7, 8, 9, 10)
print("Tuple c (a + b):", c)                                                   # (1, 2, 3, 4, 5, 5, 7, 8, 9, 10)
print("Length of tuple c:", len(c))                                            # 11
print("Count of 5 in tuple c:", c.count(5))                                    # 2
print("Index of 5 in tuple c(index 5 to 8):", c.index(5, 5, 9))                # 5