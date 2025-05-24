# print("hello")

# # strings 

# a = "A"

# # converts characters to unicode
# print(ord(a))

# #converts unicode to characters
# print(chr(65))

#indexing

# a = 4

# print(float(a))

# a = input("Enter your birth year")

# print(a)


#comparion value

# a = 12
# b= 12

# print(a != b)
# print(45 > 5)

#if-else

#a = 15

#if a > 564:
    #print("a is greater than 5")

#else:
    #print("a is less than 5")    

#icecream = int(input("how many icecreams you have ?"))

#if icecream == 1:
#    print("give to me")

#else:
#    print("give to every one")


#gender = str(input("enter your gender"))

#if gender == "male":
 #   print("good morning Sir")
#elif gender == "female":
 #   print("good moring Mam")  
 # else:
 # print("give a valid gender")  

#number = int(input("enter your number"))

#if number % 2 == 0:
#    print("number is even")
#else:
#    print("number is odd")    #

# for loop

#d = range( 20,50 ,2)
#for i in d:
#    print(i)

#n = int(input("enter a number..."))
#for i in range(n):
#    print("hello world")

#n = int(input("enter a  number...")) 

#for i in range(0 , n , 1):
#    print(i)

#n = 10
#for i in range(10 , 0 , -1):
#    print(i)

#n = int(input("enter a number to prints it number ."))

#for i in range( n , n*11 , n):
#    print(i)

#n = int(input("enter a number"))
#sum = 0
#for i in range(1 ,n+1):
#    sum = sum + i
#    print(sum)

#n = int(input("enter a number"))

#sum = 0

#for i in range(1 , n+1):
#    sum = sum + i
    

#print(sum)    

# n = int(input("enter a number"))

# fact = 1

# for i in range(1 , n+ 1):
#     fact = fact * i

# print(fact)    


# n = int(input("enter a number"))
# even = 0
# odd = 0

# for i in range(1 , n+1):
#     if i%2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1 

# print(even , odd)  



#OOPS

# oops is a system in which we divide code in object objects are data they have functions data 

#why oops
#as code grows managing functions and global variable become messy

#classes


# class Animal:
#     type = "Cat"  # Attribute

#     def sound(self):  # Method
#         print("Meow!")

# # Directly accessing attribute and method using the class
# print(Animal().type)   # Access attribute
# Animal().sound()      

# classes are basically template or blue prints of objects or instance

# class data:
#     def __init__(self,name,age):
#         print(self)
#         self.name = name
#         self.age = age

# person1 = data("suleman" , 18)

# print(person1.age , person1.name )

#basically self is use to target the location of abject


#Constructor or initializer

# in classes we cant directly have parameters like function so for that we use constructor , it is runn on auto when we call a class 

# def __init__(self , name , age);
#     selt.name = name
   
#1  inheritance

# this is called inheritance were we assign parent class to child 

# class InternationalIndustry:
#     a = "I am attribute"
#     def greeting(self):
#         print("hello good morning")

# class national(InternationalIndustry):
#     pass

# obj1 = national()

# print(national.a)

# classmethods are use to target the place of class this cls

#    constructor in inheritance
        #  parent constructor is also use by child

#single 

#multi inheritance

# class NationalFactory:
#     def __init__(self,material,color):
#         self.material = material
#         self.color = color

# class ProvenceFactory(NationalFactory):
#     def __init__(self, material, color,zips):
#         super().__init__(material, color)
#         self.zips= zips

#MRO method resolution order

#multilevel 

# class NationalFactory:
#     def __init__(self,material,color):
#         self.material = material
#         self.color = color

# class ProvenceFactory(NationalFactory):
#     def __init__(self, material, color,zips):
#         super().__init__(material, color)
#         self.zips= zips

# class CityFactory(ProvenceFactory):
#     def __init__(self, material, color, zips , pockets):
#         super().__init__(material, color, zips)      
#         self.pockets= pockets

# bag1 = CityFactory("plastic" , "red" , 2 , 4)

# print("Material:", bag1.material)
# print("Color:", bag1.color)
# print("Zips:", bag1.zips)
# print("Pockets:", bag1.pockets)

#Polymorphism

# python overwrite the function aur variable of same names 

# same thing but work different at different context

# it can only be achieved by 2 ways because python dont support overloading

#first way method overriding 

# if same name function aur attribute is in parent and child on accessing that it will give child like overriding 



# class Animal:
#     def show():
#         print("I am suleman")

# class Human(Animal):
#     def show(self):
#         print("I am suleman")   

# class Animal:
#     def show():
#         print("I am showing")


# duck typing


# "If it looks like a duck, swims like a duck, and quacks like a duck, it's probably a duck."

# In Python, you don’t care what type an object is — you only care if it behaves correctly

# ENCAPSULATION

