# Reminders:
#   Quiz this Friday, Dictionaries
#   Final Project Design Document Due Monday, November 16 (2 weeks)
# Homework: Assigned -- Classes


from dataclasses import dataclass

@dataclass
class Example:
    a: int
    s: str

    def up(self):
        self.a += 2

    def down(self):
        self.a -= 5

    def better(self,other):
        if self.s < other.s:
            self.a += other.a
        else:
            self.a -= other.a


def main():
    x = Example(6,'r')
    y = Example(3,'q')

    x.up()
    x.up()
    y.down()
    x.down()
    x.better(y)
    y.better(x)

    print(x.a)
    print(y.a)

main()


# Designing You Own Class

# We are going to build a 'Fountain' Class, representing a real-world water fountain.
# Each Fountain object has three parameters:
# -- a capacity -- an int, with how many liters of water the fountain can hold
# -- current -- an int, the current number of liters in the fountain
# -- running -- a boolean, which is True if the fountain is currently running

# we then have a few methods:
# -- drain(), which removes all water from the fountain
# -- add(n: int) which adds n liters of water to the fountain (if this is too much, extra is wasted)
# -- toggle() -- turns a running fountain off, and an off fountain on, except:
#       -- a fountain cannot run if there is no water
# -- get_status() prints a message to the user describing the state of the fountain
