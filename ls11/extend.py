class A: 
    a = "12"

    def af():
        print("af")

class B(A):
    b = "10"

a = A()
b = B()

print(a.a, b.a, b.b)
b.af