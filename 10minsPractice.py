import math
import random
from datetime import datetime
x = 10
y = 12

print(x+y)
print(x-y)

#name = str(input('Enter your name: '))
#print(f'{name.capitalize()}')

if x == y :
    print(True)
elif x>y:
    print(True)
else:
    print(False)


for x in range(5):
    for y in range(x):
        print("x",end='')
    print()

x = 0

while x <3:
    print(x)
    x+=1

squ = [x**2 for x in range(5)]
print(squ)


for x in range(1,5):
    if x ==3:
        break
    print(x)

for x in range(1,5):
    if x ==2:
        continue
    print(x)

def greet(name):
    print(name)
greet('Taranjit')

add = lambda x,y:x+y
print(add(3,4))


def details(*key,**keys):
    print(key)# Tuple
    print(keys)# Dictionary
details(1, 2, 3, name="Taranjit", age=30)

#Lists(Mutable, Ordered):

li=[1,2,3,4,5,6]
li.append(78)
li.remove(3)
print(li)

tup=(23,34,45,22,11,45)

print(tup[3])

set1 = {23,45,22,11,45,66,767,9}
print(set1)

dic = {
    'name':'Taranjijt',
    'age':30
}

print(dic.get('age'))

for key,value in dic.items():
    print(f"{key}={value}")

class Car:
    def __init__(self,brand):
        self.brand= brand
    def classFunction(self):
         print(self.brand)

class ElectricCar(Car):
    def __init__(self,brand,factory):
        super().__init__(brand)
        self.factory=factory

objEle=ElectricCar("Tesla",'EV Truck')

print(objEle.brand,objEle.factory)

class Encasulation_Bank:
    def __init__(self,bankName):
        self.__bankName=bankName

    def getBankName(self):
        return self.__bankName

objEncapsulation = Encasulation_Bank('HDFC')
print(objEncapsulation.getBankName())

class Animal:
    def sound(self):
        return 'Some Sound'

class Dog(Animal):
    def sound(self):
        return 'Bark'

obgDog = Dog()
print(obgDog.sound())

def exption():
    try:
        x = 1/0
    except  ZeroDivisionError as e:
        print(f'cannot {e}')
    finally:
        print("Execution completed.")
exption()

print(math.sqrt(16))
print(random.randint(1,10))

print(datetime.now())

string1 = 'Taranjit Singh Bains'

def reverse_string():
    print(string1[-1:-(len(string1))-1:-1])
    print(string1[::-1])

reverse_string()
print(string1)

#Swap Two Variables Without a Temporary Variable
a= 2
b =4
print(a,b)
a,b=b,a
print(a,b)

#Find Even or Odd Number

for x in range(1,20):
    if x % 2 == 0:
        print(f"{x} is even number.")

#Check if a Number is Prime
number = 29
if number >=2:
    if number % 2 == 0:
        print('not prime number.')
    else:
        for x in range(3,int(math.sqrt(number))+1,2):
            if number%x==0:
                print('Not prime number')
                break
        else:
            print(f'{number} is prime number')
else:
    print(f'{number} is not prime number.')


def factorial(n):
   if n > 0: #base
       if n == 1:
           return 1
       fab = n * factorial(n-1)
       return fab

print(factorial(4))

"""
factorial(5) = 5 * factorial(4) = 5 * 24 = 120
factorial(4) = 4 * factorial(3) = 4 * 6 = 24
factorial(3) = 3 * factorial(2) = 3 * 2 = 6
factorial(2) = 2 * factorial(1) = 2 * 1 = 2
factorial(1) = 1
"""

string2 = 'rUn DogS'
print(string2)
string3 = ''
for x in string2:
    if x.isupper():
        string3 +=x.lower()
    else:
        string3+=x.upper()
print(string3)
