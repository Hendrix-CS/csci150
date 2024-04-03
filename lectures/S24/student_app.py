from student import Student


def main():
    data = {}
    command = ""
    while command != 'quit':
        print("1: Add student")
        print("2: List all students")
        print("3: Declare major")
        print("4: Join activity")
        print("5: Receive grade")
        print("6: View a student")
        print("7: Get student GPA")
        print("'quit' to exit")
        command = input("Enter choice: ")
        if command == '1':
            name = input("Enter student name: ")
            age = int(input("Enter age: "))
            cohort = int(input("Enter entrance year: "))
            s = Student(age, cohort)
            data[name] = s
        elif command == '2':
            for name in data:
                print(name)
        elif command == '3':
            name = input("Enter student name to declare major: ")
            major = input("Enter major: ")
            data[name].declare(major)
        elif command == '4':
            name = input("Enter student name to join activity: ")
            activity = input("Enter activity: ")
            data[name].participate_in(activity)
        elif command == '5':
            name = input("Enter student name for a grade: ")
            grade = input("Enter grade: ")
            data[name].earn_grade(grade)
        elif command == '6':
            name = input("Enter student to view: ")
            print(data[name])
        elif command == '7':
            name = input("Enter student to see GPA: ")
            print(data[name].gpa())


main()