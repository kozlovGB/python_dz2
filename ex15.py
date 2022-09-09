#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
N=int(input("Введите N: "))
m=N
sum=1
while m!=0:
    sum*=m
    m-=1
string="1, "
for i in range(1,N-1):
    string+=str(i*(i+1))+", "
string+=str(sum)
print(string)