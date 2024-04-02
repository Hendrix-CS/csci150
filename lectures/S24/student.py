class Student:
    def __init__(self, age: int, cohort: int):
        self.age = age
        self.cohort = cohort
        self.major = 'Undecided'
        self.activities = []
        self.grades = []

    def __str__(self) -> str:
        return f"age: {self.age}\ncohort: {self.cohort}\nmajor: {self.major}\nactivities: {self.activities}\ngpa: {self.gpa()}"

    def declare(self, major_name: str):
        self.major = major_name

    def participate_in(self, activity: str):
        self.activities.append(activity)

    def earn_grade(self, grade: str):
        self.grades.append(grade.upper())

    def gpa(self) -> float:
        if len(self.grades) > 0:
            grade_points = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
            total_points = 0
            for grade in self.grades:
                total_points += grade_points[grade]
            return total_points / len(self.grades)