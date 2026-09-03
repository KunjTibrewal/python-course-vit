marks = [85, 92, 78, 96, 88]
print("Marks:", marks)                                                       # [85, 92, 78, 96, 88]
print(marks[0])                                                              # 85
natural_numbers_till_10 = [i for i in range(1, 11)]                 
print("Natural numbers till 10:", natural_numbers_till_10)                   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
marks.append(90)
print("Marks after appending 90:", marks)                                    # [85, 92, 78, 96, 88, 90]
marks.sort()
print("Marks after sorting:", marks)                                         #[78, 85, 88, 90, 92, 96]
print("Length of marks list:", len(marks))                                   #6
print("Count of 88 in marks:", marks.count(88))                              #1
m = marks
m[0] = 100
print("Marks after modifying m:", marks)                                     #[100, 92, 90, 88, 85, 78]
l = marks.copy()
l[0] = 50
print("Marks after modifying l:", marks)                                     #[100, 92, 90, 88, 85, 78]  
marks.insert(2, 95)
print("Marks after inserting 95 at index 2:", marks)                         #[100, 92, 95, 90, 88, 85, 78]
marks.extend(natural_numbers_till_10)
print("Marks after extending with natural numbers till 10:", marks)          #[100, 92, 95, 90, 88, 85, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
marks.remove(natural_numbers_till_10[0])
print("Marks after removing the first natural number:", marks)               #[100, 92, 95, 90, 88, 85, 78, 2, 3, 4, 5, 6, 7, 8, 9, 10]
