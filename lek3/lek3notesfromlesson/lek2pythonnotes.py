class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y

p = Point(2, 8)

print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
people = ["a", "b", "c", "d"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print("added")
    else:
        print("not added")

#decorator add aditional behavior to function
# takes function as input
def announce(f):
    def wrapper():
        print("about to run the function")
        f()
        print ("done")
    return wrapper

@announce
def hello():
    print("hello,world")

hello()

#lamda
people = [
   {"name": "d", "house": "ath"},
   {"name": "b", "house": "thes"},
   {"name": "c", "house": "lar"},
]

def f(person):
    return person["name"]

# The `key` parameter in `sort()` specifies a function that determines the value to be used for sorting each element.
people.sort(key=f)

print(people)

# ayto: lamda person: person["name"] einai mia plhrh function poy pernei to person san input kai epistrefei to erson["name"]
people.sort(key=lambda person: person["name"])

print(people)

#exception
import sys

try:
    result = x / y
except:
    print("sdfgsfdg")
    sys.exit(1)


# basic
print("hello")
a=1
a = input("give name: ")
print(a)
print (f"my name is {a}")
