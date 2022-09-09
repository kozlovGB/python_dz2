x=float(input("Введите число: "))
string=str(x)
res_str = string.replace('.', '')# удаление дробной точки
if x<0:#проверка числа на отрицательность для избавления от минуса
    res_str = res_str.replace('-', '')
sum=0
res_int=int(res_str)
while res_int>0:
    sum+=res_int%10
    res_int=res_int//10
print(sum)