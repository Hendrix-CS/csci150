class Gradebook:

    def __init__(self):
        self.grades = []
        self.ec     = 0

    def add_grade(self, g: int):
        self.grades.append(g)

    def add_ec(self, ec: int):
        self.ec += ec

    def average(self):
        return (sum(self.grades) + self.ec)/len(self.grades)

def main():
    gb = Gradebook()
    gb.add_grade(90)
    gb.add_grade(83)
    gb.add_grade(97)
    gb.add_ec(10)

    print(gb.average())

main()
