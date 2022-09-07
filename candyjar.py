print("***************! CANDY JAR !****************")
no_of_candies=100
candies_you_want=int(input("enter how much candy you want: "))
if no_of_candies==candies_you_want:
    print("congratulations you got candies\n number of candies you purchased=" ,candies_you_want)
elif no_of_candies>candies_you_want:
    print("congratulations you got candies \nnumber of candies you purchased=",candies_you_want,"number of candies left in jar=",(no_of_candies-candies_you_want))
else:
    print("sorry I don't have sufficient amount of candies\nyour remaining candies=",(candies_you_want-no_of_candies), "\nyou will get remaining candies tommorrow")