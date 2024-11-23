i = 0

while i <= 4:
    if i == 1:
        break;
    print("hallo")
    i += 1

a = 10
b = 20
if a < b:
    print("a is small", a)
elif b > a:
    print("b is small", b)
else:
    print("nor a and b", a, b)

for i in range(2):
    print("apple")

data = ['a', 'b', 'c']
for i in data:
    print(i)
    if i == 'a':
        print(" a came")
    else:
        continue

for j in range(5):
    print(j)

print("***************************************************************************************")
print("odd")
for k in range(1, 10, 2):
    print(k)

print("***************************************************************************************")
print("even")
for k in range(1, 10):
    if k % 2 == 0:
        print(k)
    else:
        continue
print("***************************************************************************************")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


def function1():
    print("hey")


function1()


def function2(a, b):
    if a < 11:
        print("you can proceed")
        print(a + b)
    else:
        print("you can't")


function2(10, 1)


def function3(data1):
    for i in data1:
        print(i)


value = ["happy", "joy"]

function3(value)


def function4(x):
    a = x * 2;
    return a


q = function4(6)
print(q)

print("***************************************************************************************")


def function5():
    pass


a = [3, 4, 5, 1, 2]
a.sort()
print(a)
a.reverse()
print(a)


def recursionfn(i):
    if i > 0:
        res = recursionfn(i - 1)
        print(i)
    else:
        print("else")
        print(i)


recursionfn(5)
print("***************************************************************************************")

list1 = ["data1", 1, 2, 3, 4, 's', "zish"]
print(list1)

list1.append("last")
print(list1)

list1.pop(0)
print(list1)

list1.remove("last")
print(list1)
print("***************************************************************************************")


class Forest:
    def __init__(self, animal):
        self.animal = animal


instance1 = Forest("tiger")

print(instance1.animal)

print("***************************************************************************************")
try:
    print("try")
except:
    print("catch")
else:
    print("finally")
"""

print("***************************************************************************************")

x1 = "good"
if not type(x1) is int:
    raise TypeError("Only integer is allowed")


print("***************************************************************************************")
x = -2
if x < 0:
    raise Exception("no number , sorry")



number1 = int(input("no 1"))
number2 = int(input("no 2"))
sum = number1+number2
print(sum)
for i in range(2):
    sum+=sum
    print(sum)

print(f"value is {sum}")
"""

fruit = "mango"
print(fruit.upper())
print(fruit.lower())


q =int(333.3)
print(q)


listOfElements = [2,54,45.4,64,4,7,1]
listOfElements.sort()

print("***************************************************************************************")
print(f"sorted list is {listOfElements}")
for i in listOfElements:
    print(i)


print("***************************************************************************************")
print(listOfElements[0:2])
print(listOfElements[:])
print(listOfElements[:2])
print(listOfElements[0:])
print("***************************************************************************************")

tuple1 = (1,2,3,"a")
print(tuple1)

print(tuple1.index(1))
print(tuple1.count(3))

print("***************************************************************************************")

dic = {
    "value": 1,
    "value2":2
}

print(dic)
print(dic["value"])