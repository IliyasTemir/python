# Booleans 
print(8 > 2)
print(6 == 9)
print(3 < 1)


c = 700
d = 99
if d > c:
  print("d is greater than c")
else:
  print("d is not greater than c")

# Boolean values
print(bool("World"))
print(bool(15))

p = "World"
q = 27

print(bool(p))
print(bool(q))

bool("xyz")
bool(789)
bool(["grape", "melon", "plum"])


class mynewclass():
  def __len__(self):
    return 0

mynewobj = mynewclass()
print(bool(mynewobj))

def anotherFunction():
  return False

if anotherFunction():
  print("CORRECT!")
else:
  print("WRONG!")

m = 500
print(isinstance(m, float))

# Operators
print(9 + 6)
print(33 + 7 * 3)
print(8 + 4 - 2 + 9)

# Lists
cars = ["bmw", "audi", "nissan"]
print(cars)

listA = ["pineapple", "mango", "grape"]
listB = [9, 8, 2, 1, 5]
listC = [False, False, True]

# Tuples
tupleX = ("peach", "mango", "fig")
print(tupleX)

r = ("plum", "grape", "kiwi")
s = list(r)
s[1] = "strawberry"
r = tuple(s)

print(r)

tupleD = ("x", "y", "z")
tupleE = (7, 8, 9)

tupleF = tupleD + tupleE
print(tupleF)

# Sets
fruitSet = {"mango", "grape", "strawberry"}
print(fruitSet)

setX = {"banana", "melon", "plum"}
setY = {1, 3, 7, 6, 2}
setZ = {False, False, True}

fruitSet = {"apple", "kiwi", "plum"}

for item in fruitSet:
  print(item)

# Dictionaries
cardict = {
  "brand": "Tesla",
  "model": "Model S",
  "year": 2022
}

auto = {
"brand": "Honda",
"model": "Civic",
"year": 2021
}
n = auto.keys()

print(n) # before the change

auto["color"] = "blue"
print(n) # after the change

# If ... Else 
A = 120
B = 330
if B > A:
  print("B is greater than A")

A = 99
B = 99
if B > A:
  print("B is greater than A")
elif A == B:
  print("A and B are equal")

# While Loops
i = 2
while i < 6:
  print(i)
  i += 1

i = 2
while i < 7:
  print(i)
  if i == 3:
    break
  i += 1

i = 1
while i < 6:
  i += 1
  if i == 4:
    continue
  print(i)
  
# For Loops

electronics = ["phone", "tablet", "laptop"]
for x in electronics:
  print(x)

for x in range(1, 20, 2):
  print(x)

foods = ["burger", "pasta", "noodles"]
for x in foods:
  print(x)
  if x == "pasta":
    break

for x in range(5):
  print(x)
else:
  print("Finally done!")

colors = ["red", "blue", "yellow"]
objects = ["ball", "chair", "pen"]

for x in colors:
  for y in objects:
    print(x, y)
