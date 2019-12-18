# List can contain strings integer or float points
# Python index begins from zero

a =["string","int",1,2]

#indexing a list
a[2]
print(a[2])
# Returns all the values of a
b = a[:]

print(b)

#Overwriting values in a string

a[1] = "glo"
print(a)

print(b)

# Skipping one item from a list
a =[1,2,3,4,5,6,7,8,9,10]
# Side note first position is always inclusive while the last position is always exclusive
val = a[2:4]
print(val)
# Print subset of zero to four but skip three values while printing
val = a[0:4:3]
print(val)
# Print subset of zero to nine but skip three values while printing
#It skips three intermittently
# n:n-1
val = a[0:10:3]
print(val)
# Negative value prints backward
val = a[-2]
print(val)
# Findout how to use range of negative numbers
#val = a[-1:-3]
print(val)