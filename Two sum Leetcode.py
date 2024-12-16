print("Enter the value:")
value=int(input())
print("Enter the target:")
target=int(input())
num=[]
list1=[]
print("List are:")
for i in range(value):
   x=int(input())
   num.append(x)
print(num)
for j in range(len(num)):
    for k in range(j):
     if(j<value and k<value):
        if(num[j]+num[k]==target):
            list1.append(k)
            list1.append(j)
    
print(list1)
