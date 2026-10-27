class A:
    def list1(self):
        l=[56,61,45,32]
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if l[j]<l[i]:
                    temp=l[i]
                    l[i]=l[j]
                    l[j]=temp

        print("Sorted list is:",l)

class B:
    def list1(self):
        super().list1()
        l=[32,41,16]
        l1=[65,54,21]
        d={}

        for i in range(len(l)):
                d[l[i]]=l1[i]

        print("List Converted to Dict is:",d)

class C(B,A):
    def list1(self):
        super().list1() 
        l=[1,2,3,1,2]
        uni=[]

        for i in l:
            if i not in uni:
                uni.append(i)
        print("Unique ans is:",uni)


obj=C()
obj.list1()

