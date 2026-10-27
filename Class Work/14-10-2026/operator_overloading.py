class User:

    def __init__(self,a,b):
        # print("Init called,constructor")
        self.a=a
        self.b=b

    def __str__(self):
        return f"{self.a},{self.b}"

    def __add__(self,obj):
        x= self.a+obj.a
        y= self.b+obj.b

        return User(x,y)

    def __sub__(self,obj):
        x= self.a-obj.a
        y= self.b-obj.b 

        return User(x,y)            

    def __mul__(self,obj):
        x= self.a*obj.a
        y= self.b*obj.b
        return User(x,y)    
    
    def __truediv__(self,obj):
        x= self.a/obj.a
        y= self.b/obj.b     
        return User(x,y)
    

obj=User(50,100)
print(obj)

obj1=User(10,20)
print(obj1)

print("Addition is:",obj+obj1)
print("Subtraction is:",obj-obj1)
print("Multiplication is:",obj*obj1)
print("Division is:",obj/obj1)
