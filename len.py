# Gets length of a string
top = ["fjfjjffj","dkddkddkdkd"]
print(len(top))
# list all the methods associated to an object
top.clear()
print(top)
#get notation is more preferable than brackets while calling dictionary values
num1=[24,15,5,9,18]
num2=[7,3,12,8,2]
num3=[]
num4=[]
def arrange():
    for num in num1:
        if num % 2 ==0:
            num3.append(num)
    for num in num2:
        if num % 2 !=0:
            num3.append(num)
    return num3

print(arrange())