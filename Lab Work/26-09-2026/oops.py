# class pattern:
#     def angle(self):    #self instance variable agar #idhar self diye do niche bhi bracket
#         for i in range(1,6):
#             print("*"*i)

# p=pattern() #ye brcaket self ki wajah se hai.
# p.angle()


class Pattern:
    def left_angle():
        for i in range(1,6):

            for k in range(1,6-i):
                print(" ",end=" ")

            for j in range(1,i+1):
                print("*",end=" ")

            print()

        # for i in range(4,0,-1):

        #     for k in range(1,6-i):
        #         print(" ",end="")

        #     for j in range(1,i+1):
        #         print("*",end="")

        # print()

p=Pattern
p.left_angle()