"""
    Adding two stringss
"""

def add(firstname,lastname):
    return (firstname+lastname)


print(add("Mike","Hazard"))


"""
Multiplying a string
"""

def hello(name):
    symbol = "**************************"
    print(symbol)
    print(name)
    print(symbol)

hello("python")

"""
    Slicing a string
"""
name ="Aaron"
print(name[0])

"""
Checking string type
"""
print(type(name))


"""
Get the length of a string
"""
info ="It will probably rain today"
print(len(info))

"""
Capitalize the first letter of the string string
"""
print(info.capitalize())


"""
Capitalize every letter of the string string
"""
print(info.upper())