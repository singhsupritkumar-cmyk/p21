###  single level inheritance 

# class a():
#     def greet(self):
#         print("hello how are you")

# class b(a):
#     pass

# obj=b()
# obj.greet()
 

# class reebook():
#     def show(self):
#         print("this is reebook company")
    
#     def bag(self):
#         print("reebook manufacture baga")

# class bata(reebook):
#     def show2(self):
#         print("this is baya class inheritance by reebook class")

# person1=reebook()
# person1.show()

# person2 =bata()
# person2.show()
# person2.bag()


### multiple inheritance


# class parents1():
#     def show1(self):
#         print("this is parents class")

# class parents2():
#     def show2(self):
#         print("this is parents class")

# class child (parents1,parents2):
#     def show3(self):
#         print("this is child class")

# obj=child()
# obj.show1()
# obj.show2()
# obj.show3()

     ####


class factory():
    def __init__(self,location ,capacity):
        self.location=location
        self.capacity=capacity

    def show(self):
        print(f"this is factory class with{self.location} and{self.capacity}")

class reebook(factory):
    def __init__(self, location, capacity,brand_name):
        super().__init__(location,capacity)
        self.brand_name=brand_name

    def show2(self):
        print(f"this is reebook class with{self.location} and{self.capacity} and {self.brand_name}")


obj=reebook("mumbai",23.3,"ms dhoni")
obj.show2()

obj=factory()
    
          ##

# class a:
#     def show(self):
#         print("this is a class")

#     def details(self):
#         print("this is suprtparent class")

# class b(a):
#     def show2(self):
#         print("this is b class")

# class c(b):
#     pass

# obj =c()
# obj.show2()
# obj.details()
# obj.show()

      ##

# class a:
#     def show(swlf):
#         print("this is show method")
#     def __init__(self):
#         print("this is parent class")

# class b(a):
#     def __init__(self):
#         print("this is b class")

# class c(b):
#     def __init__(self):
#         b. __init__(self)
#         a. __init__(self)                           ##__init__   called dunder method
#         print("this is c class")
    
# obj=c()
# obj.show()


###    hieracal  inheritance

# class a():
#     def show(self):
#         print("this is a class")

# class b(a):
#     def show2(self):
#         print("thus is b class")

# class c(a):
#     pass

# obj=c()
# obj.show()



# class factory():
#     def __init__(self,name,location):
#         self.name =name
#         self.location=location

#         def show(self):
#              print(f"{self.name} and {self.location}")

# class shoe(factory):
#     def __init__(self, name, location,shoe_size):
#         super().__init__(name, location)
#         self.shoe_size =shoe_size

#     def show2(self):
#         print(f"{self.name}{self.location}{self.shoe_size}")

# class tshirt(factory):
#     def __init__(self, name, location,tshirt_color):
#         super().__init__(name, location)
#         self.tshirt_color =tshirt_color 

# def show3(self):
#     print(f"{self.name}{self.location}{self.tshit_color}")

# obj=tshirt ("shaktiman",'girdhan ghat','black')
# obj.show()
# obj.show3()

# obj2=shoe("flying jatt",'punjab',40)
# obj2.show()
# obj2.show2()


####### poly morphism 


# class animal():
#     def show(self):
#         print("this is animal class")

#     def show(self,name):
#         self.name=name
#         print(f"{self.name}")

#     def show(self):
#         print("this is animal class")


# class dog(animal):
#     def show(self):
#         print("this is dog class")

#         ## method overloading- not supported by python


# # obj=dog()
# # obj.show()

# obj=animal()
# obj.show()


##                   duck typing


# class animal():
#     def show(self):
#         print("this is annimal class")

# class dog():
#     def show(self):
#         print("this is dog class")

# obj=animal()
# obj.show()

# obj=dog()
# obj.show()


# class employee():
#     def __init__(self,name):
#         self.name=name
    
# def show_details(self):
#     print(f"this is employee class{self.name}")

# class developer(employee):
#     def __init__(self, name,programmimg):
#         super().__init__(name)
#         self.programming =programmimg

# class manager(employee):
#     def __init__(self, name,team_size):
#         super().__init__(name)
#         self.team_size=team_size

# def show_details(self):
#     print(f"this is manager class{self.name}and {self.team_size}")

# obj=developer('suprit','python')
# obj2=manager('payal',20)
# obj.show_details()


