# Adding two list
a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = [a+b]
print(c)

#Adding two turples

a =(1,2,3)
b = (1,2,3)
c = a+b
print(c)
# Adding two maps

a ={'a':"Mike",'b':"Jane"}
b ={'c':"Jane",'d':"Lucy"}
# double asteriks for turple Single asteriks for list
c ={**a,**b}
print(c)
#help(map)
# Extracting values from two or more maps and joining them together
c = {a['a'],b['d']}
print(c)
