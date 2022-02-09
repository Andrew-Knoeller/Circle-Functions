# Program that uses functions to calculate perimeter and/or area of a given circle
# uses a try/except to catch invalid input
# 02/09/2022

def calcPerimeter(r):
    r = float(r)
    perimeter = 2*3.14*r
    return perimeter

def calcArea(r):
    r = float(r)
    area = 3.14*r**2
    return area

x = input("Enter radius to calculate perimeter: ")
while True:
    try:
        x = calcPerimeter(x)
        break
    except ValueError:
        print("Sorry enter a number")
        x = input("Enter radius to calculate perimeter: ")

y = input("Enter radius to calculate area of the circle: ")
while True:
    try:
        y = calcArea(y)
        break
    except:
        print("Sorry enter a number")
        y = input("Enter radius to calculate area of the circle: ")


print("The perimeter of the circle ", x)
print("The area of the circle is ", y)

input("Press any key") 