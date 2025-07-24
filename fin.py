from typing import final
class Animal:
    def sound(self):
        print("Animal sound")
class Bird:
    @final
    def sound(self):
        print("Bird chirping")

# Example usage
if __name__ == "__main__":
    a = Animal()
    a.sound()
    b = Bird()
    b.sound()

