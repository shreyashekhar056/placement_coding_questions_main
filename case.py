import math
def display_menu():
    print("#1 circle")
    print("#2 square")
    print("#3 traingle ")
    print("#4 rectangle")

def area_circle():
    r=float(input("enter radius:"))
    area = math.pi * r * r
    print(f"Area: {area:.2f}")

def area_square():
    s=float(input("enter side:"))
    area = s * s
    print(f"Area: {area:.2f}")

def area_traingle():
    b=float(input("enter base:"))
    h=float(input("enter height:"))
    area = 0.5*b*h
    print(f"Area: {area:.2f}")

def area_rectangle():
    l =float(input("enter length:"))
    b=float(input("enter breadth:"))

while True:
    display_menu()

    ch = int(input("Enter your choice"))
    if ch == 1:
        area_circle()
    elif ch == 2:
        area_square()
    elif ch == 3:
        area_traingle()
    elif ch == 4:
        area_rectangle()

    elif ch == 5:
        print("thankyou exit")
        break
    else:
        print("invalid choice")

