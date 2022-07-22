from area import *

while True :
    print("1.Circle")
    print("2.Reactangle")
    print("3.Triangle")
    
    choice = int(input("Enter the choice : "))
    
    if choice == 1 :
        c = int(input("Enter the Radius : "))
        t = ar_circle(c)
        print(t)
    elif choice == 2 :
        l = int(input("Enter the L : "))
        b = int(input("Enter the B : "))
        y = ar_rect(l , b)
        print(y)
    elif choice == 3 :
        b = int(input("Enter the Base : "))
        h = int(input("Enter the Height : "))
        q = ar_tri(b , h)
        print(q)
    else :
        print("Enter the Valid choice!")