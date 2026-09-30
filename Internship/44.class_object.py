class Right:
    def right_angle():
        for i in range(1,6):
            print("*"*i)

r=Right
print("Right angle pattern:")
r.right_angle()

class Left:
    def left_angle():
        for i in range(1,6):
            print(" "*(6-i),"*"*i)

l=Left
print("Left angle pattern:")
l.left_angle()

class Triangle:
    def triangle():
        for i in range(1,6):
            print(" "*(6-i)," *"*i)

t=Triangle
print("Triangle pattern:")
t.triangle()

class Square:
    def square():
        for i in range(1,6):
            for i in range(1,6):
                print("*",end=" ")

            print()

s=Square
print("Square pattern:")
s.square()


class Diamond:
    def diamond():
        for i in range(1,6):

            for k in range(1,6-i):
                print(" ",end="")

            for j in range(1,i+1):
                print("*",end=" ")

            print()

        for i in range(4,0,-1):

            for k in range(1,6-i):
                print(" ",end="")

            for j in range(1,i+1):
                print("*",end=" ")

            print()

d=Diamond
print("Diamond:")
d.diamond()

class HourTime:
    print("Hour Pattern:")
    def hourtime():
        for i in range(1,6):
            for k in range(1,6-i):
                print(" ",end="")
        
            for j in range(1,i+1):
                print("*",end=" ")
        
            print()
        
    for i in range(5,0,-1):
        
        for k in range(1,6-i):
            print(" ",end="")
        
        for j in range(1,i+1):
            print("*",end=" ")
        
        print()

h=HourTime
h.hourtime()