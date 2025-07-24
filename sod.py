class A:
    def isprime(self, n):
        self.a = n  # Added to make self.a available
        if self.a < 2:
            return False
        for i in range(2, self.a):  # Avoid division by zero and 1
            if (self.a % i == 0):
                return False
        return True

class B(A):
    def sod(self, a):  # Changed parameter to 'a' to match assignment
        self.a = a     # This is needed for self.a to exist
        return sum([int(i) for i in str(self.a)])

s1 = B()
print(s1.isprime(37))     # Output: True
print(s1.sod(12345))      # Output: 15

class C(A, B):
    def show(self):       # Added self parameter
        print("hello")

xx = B()
print(xx.isprime(29))     # Added number as parameter
