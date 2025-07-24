class A:
    def display(self):
        print("Hello")
class B(A):
    def show(self):
        print("how are you?")

s1=A()
s2=B()

s2.display()  # This will raise an AttributeError