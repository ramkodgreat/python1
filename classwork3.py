score= int(input('pls enter ur score'))
if score>400:
    print("Invalid score")
elif score<180:
    print("You are not qualified")
elif score==180:
    print("Geop")
elif score==250:
    print("pharmacy")
elif score==350:
    print("Medcine")
elif score==400:
    print("Computer science")
else:
    print("Sorry we dont have a course for you see the registrar")
