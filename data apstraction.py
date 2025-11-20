from abc import ABC, abstractmethod 

# class animal(ABC):

## abc=abstract class

#     @abstractmethod
#     def make_sound(self):
#         pass

# class dog(animal):
#     def make_sound(self):
#         print("dog class")

# obj=dog()
# obj.make_sound()


# class payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass

# class paytm(payment):
#     def pay(self):
#         print("paytm makes payment")

# class phonepe(payment):
#     def pay(self):
#         print("phonepr makes payment")

# paytm=paytm()
# phonepe=phonepe()
# paytm.pay()
# phonepe.pay()


# class demo(ABC):        #abstract class
#     @abstractmethod
#     def show():
#         pass

# class demo2(demo):
#     def show(self):
#         print("this is demo2 class")

# obj=demo2()
# obj.show()


# class rule (ABC):       ##abstract class
#     @abstractmethod
#     def perimeter(self):
#         pass

#     @abstractmethod
#     def area(self):  ## abstract class
#         pass


# class square:
#     def __init__(self,s):
#         self.s=s

#     def area(self):
#         print(f"this is are class{self.s}")

#     def perimeter(self):
#         print(f"this is perimeter method{self.s}")

# class circle:
#     def __init__(self,r):
#         self.r=r

# obj=square(10)
# obj.area()
# obj.perimeter()



# class animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class dog(animal):
#     def make_sound(self):
#         print("this is dog class")

# class lion(animal):
#     def make_sound(self):
#         print("this is lion class")

# obj=dog()
# obj.make_sound()

# obj=lion()
# obj.make_sound()