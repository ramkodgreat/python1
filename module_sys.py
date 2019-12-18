import sys
# Sys modules collect inputs
def message():
    print("Enter your name in full")
    name = sys.stdin.readline()
    print("Enter your age")
    age = int(sys.stdin.readline())
    print("Thank you %s and you are %d yearsold"%(name,age))

message()