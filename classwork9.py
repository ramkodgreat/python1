#def hobbies():
hobbies = input("Enter your hobbies seperated by commas")
hobbies_list = hobbies.split()
print(hobbies_list)

#hobbies()

for hobby in hobbies_list:
    print(hobby) #individual hoo
    for hobbies in hobby:
        print(len(hobbies))
    #for len(hobbies[:]) > hobby:
        #print(hobbies)

    