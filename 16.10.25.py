list1=[1,2,3,4,5,6]
for i in range(5,-1,-1):
    print(list1[i])
count=0
for i in list1:
    if i%2==0:
        count+=1
print(count)
summa=0
for i in list1:
    summa+=i
print(summa)
max=list1[0]
max_index=0
for i in range(len(list1)):
    if max<list1[i]:
        max=list1[i]
        max_index=i
print(max_index)
list1=[5,6,78,25,25,7,8,9]
_min=int(input("Введите минимальное значение"))
_max=int(input("Введите максимальнон значение"))
if _min>_max:
            _min,_max=_max,_min
for i in list1:
    if _min<=i<=_max:
       print(i, end="")
#функции
list1=[2,5,6,7,8,9,7,12]
def change_even_val(_list):
    for i in range(len(_list)):
        if _list[i]%2==0:
            _list[i]=0
            print(list1)
            change_even_val(list1)
            print(list1)
def change_max_val(a,b):
    print(a,b)
a=5
b=9
print(a,b)
change_max_val(a,b)




