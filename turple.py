# Turple is not as flexible as list
# Turple uses parenthesis instead of square brackets like a list
# its more like constants
a =(1,2,3,4,5,6,7,8,9,10)
#Indexing elements of a turple
val = a[2]
print(val)

# Returning all elements of a turple
val = a[:]
print(val)

#Overwrite value in a turple
#a[1] = 40
#print(a) Side note you cant write to a turple

#Printing one item from the list
val = a[2:4]
print(val)

# Appending to a turple does not work
#a.append(9)
#print(a)
# Pop does not work on a turplessss
#a.pop()
#print(a)
# Getting the last element#
val = a[-1]
print(val)
# Range of 2-4
val = a[1:6:2]
print(val)