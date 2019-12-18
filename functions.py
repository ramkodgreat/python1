# Functions perform a particular task
# Coponents of a function
# def keyword
#Parameters/arguments
#function name
#body of the function
# signstures are parameters that make a function works

def test():
    print("hello")

test()

def test_two(a,b):
    print(a,b)

test_two("Hello","world")

def testfunc(myname):
    print("hello %s"%myname)

testfunc("nurudeen")

def fullname(myname,surname):
    print("hello %s"%myname,surname)
    return


fullname("Nurudeen","Akindele")
def volume(l,b):
    area =l*b
    print(area)
    
volume(67,3)    

def test_three(a):
    return a
b = test_three(2)
print(b)
# Return is used as break in a function
def come(a):
    if a<5:
        return a
    else: 
        a > 10
        print("good")
come(11)

def test():
    print("This is yahoo")
    return
    print("This is google") 

test()

def a():
    return 5

def test(*a):
    print(a)
test(1,2,3,5)
def test(**a):
    print(a)


#a ={"a":"Sam","b":"Delilah"}
#test(**a)

#Copying a list to a function

#a ={"a":"Sam","b":"Delilah"}
test(a="Sam",b="Delilah")
