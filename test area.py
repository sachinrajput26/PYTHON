from area import *
print("press 1: area of circle \npress 2: circumference of circle\npress 3: area of square\npress 4: area of rectangle\npress 5: perimeter of square\npress 6: perimeter of rectangle\npress 7: area of cylinder\npress 8: exit")
ch=int(input("enter your choice: "))
while ch<=8:
    if ch==1:
        radius=float(input("enter radius: "))
        area=circle(radius)
        print(" area of circle :",area)
        
    if ch==2:
        radius=float(input("enter radius: "))
        CIRCUMFERENCE=circumference(radius)
        print("circumference of circle:",CIRCUMFERENCE)
        
    if ch==3:
        l=float(input("enter value of length: "))
        area=square(l)
        print("area of square:",area)
        
    if ch==4:
        l=float(input("enter value for length: "))
        b=float(input("enter value for breadth: "))
        area=rectangle(l, b)
        print("area of rectangle :",area)
        
    elif ch==5:
        l=float(input("enter value for length: "))
        perimeter=p_square(l)
        print("perimeter of square: ", perimeter)
        
    elif ch==6:
        l=float(input("enter value for length: "))
        b=float(input("enter value for breadth: "))
        perimeter=P_rectangle(l, b)
        print("perimeter of rectangle : ",perimeter)
        
    elif ch==7:
        r=float(input("enter value for radius: "))
        h=float(input("enter value for height: "))
        area=a_cylinder(r,h)
        print("area of cylinder: ",area)
    else:
        exit()
    ch=ch+1

