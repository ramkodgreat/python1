"""
    Function to divide two list into two
    Merging the two sub list and getting
    the sum of individual sub list
"""
list = [1,2,3,4,5,6,7,8,]
def divide(list):
    if len(list) % 2 !=0:
        print("List must be divisible by two")
    else:
        mid = len(list) / 2
        sub_a = list[0:int(mid)]
        sub_b = list[int(mid):len(list)]
        new_list = [sub_a,sub_b]
        print(new_list)
        print([sum(sub_a)],[sum(sub_b)])

divide(list) 