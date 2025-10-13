list1=[2,9,15,2,4,5,15]
counter=0
for i in range(len(list1)):
    for j in range(len(list1)):
        if i==j:
           continue
        if list1[i]==list1[j]:
            counter+=1
            break
print(len(list1)-counter)
# перевернуть массив
list1=[2,9,15,2,4,5,15,2]
print(list1)
for i in range(len(list1)//2):
    list1[i],list1[len(list1)-i-1]=list1[len(list1)-i-1],list1[i]
print(list1)
#посчитать среднее значение всех эл-тов
list1=[2,9,15,2,4,5,15,2]
summa=0
for i in list1:
    summa+=i
print(summa/len(list1))
#вывести эл-ты первого списка, которые отсутсвуют во втором
list1=[5,4,3,2,1,5]
list2=[4,3,5,5,5,5]
print(list1)
print(list2)
for i in list1:
    for j in list2:
        if i==j:
         print(i, end=" ")
         break
#пОЛЬЗОВАТЕЛЬ ВВОДИТ ЧИСЛО, ОПРЕДЕЛИТЬ СКОЛЬКО РЗ ВСТРЕЧАНТСЯ ЭТО ЧИСЛО В СПИСКЕ
list1=[1,3,2,4,23,4,2,4,2]
num=int(input("введите любое число"))
counter=0
for i in list1:
    if num==i:
        counter+=1
print(counter)
#Try_except
list1=[3,4,2]
try:
    print(list1[3])
except:
    print("ошибка индекса")
    print("продолжение программы")
#
try:
    num=int(input("введите число"))
    print("число")
except:
    print("НЕ ЧИСЛО")