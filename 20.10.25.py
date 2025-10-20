students = [
    [60,77,80,90],
    [60,55,56,70],
    [78,89,97,87]
]
for i in students[0]:
     print(i,end=" ")
print()
for i in students[1]:
    print(i, end=" ")
print()
for i in students[2]:
        print(i, end=" ")
print()

students = [[60, 77, 80, 90],
            [60, 55, 56, 70],
            [78, 89, 97, 87]
]
for i in students:
    for j in i:
        print(j, end=" ")
    print()

for i in range(0,3):
    print(students[i][1])
