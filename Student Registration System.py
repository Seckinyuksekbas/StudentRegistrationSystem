import datetime

# creates a student object , with number,fname,lname,birth,gender,country attributes and getter setter methods
class Student:
    def __init__(self, student_number, first_name, last_name, date_of_birth, sex, country_of_birth):
        self._student_number = student_number
        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._sex = sex
        self._country_of_birth = country_of_birth

    def get_student_number(self):
        return self._student_number

    def set_student_number(self, student_number):
        self._student_number = student_number

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_date_of_birth(self):
        return self._date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    def get_sex(self):
        return self._sex

    def set_sex(self, sex):
        self._sex = sex

    def get_country_of_birth(self):
        return self._country_of_birth

    def set_country_of_birth(self, country_of_birth):
        self._country_of_birth = country_of_birth

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self._date_of_birth.year
        if today < datetime.date(today.year, self._date_of_birth.month, self._date_of_birth.day):
            age -= 1
        return age

# writes students list  to students.txt file
def write_to_file(students):
    with open("students.txt", "w") as f:
        for student in students:
            f.write(f"{student.get_student_number()} {student.get_first_name()} {student.get_last_name()} "
                    f"{student.get_date_of_birth().strftime('%Y-%m-%d')} {student.get_sex()} {student.get_country_of_birth()}\n")
    print("Student data written to file.")

# read from student file ,students file's texts writen into newly created students list
def read_from_file():
    students = []
    try:
        with open("students.txt", "r") as f:
            for line in f:
                fields = line.split()
                student_number = int(fields[0])
                first_name = fields[1]
                last_name = fields[2]
                date_of_birth = datetime.datetime.strptime(fields[3], "%Y-%m-%d").date()
                sex = fields[4]
                country_of_birth = fields[5]
                student = Student(student_number, first_name, last_name, date_of_birth, sex, country_of_birth)
                students.append(student)
        print("Student data read from file.")
    except FileNotFoundError:
        print("File not found.")
    return students

# checks list size and creats  a student tuple then adds tuple to students list
def add_student(students):
    if len(students) >= 100:
        print("Student array is full.")
        return
    student_number = int(input("Enter student number: "))
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    date_of_birth_str = input("Enter date of birth (YYYY-MM-DD): ")
    date_of_birth = datetime.datetime.strptime(date_of_birth_str, "%Y-%m-%d").date()
    sex = input("Enter sex (M/F): ")
    country_of_birth = input("Enter country of birth: ")
    student = Student(student_number, first_name, last_name, date_of_birth, sex, country_of_birth)
    students.append(student)

# searchs tuples in students list by number input
def find_student(students):
    student_number = int(input("Enter student number: "))
    for student in students:
        if student.get_student_number() == student_number:
            print(f"Student number: {student.get_student_number()}")
            print(f"First name: {student.get_first_name()}")
            print(f"Last name: {student.get_last_name()}")
            print(f"Date of birth: {student.get_date_of_birth().strftime('%Y-%m-%d')}")
            print(f"Age: {student.get_age()}")
            print(f"Sex: {student.get_sex()}")
            print(f"Country of birth: {student.get_country_of_birth()}")
            return
    print("Student not found.")

# prints all the tuples in students list
def show_all_students(students):
    for student in students:
        print(f"Student number: {student.get_student_number()}")
        print(f"First name: {student.get_first_name()}")
        print(f"Last name: {student.get_last_name()}")
        print(f"Date of birth: {student.get_date_of_birth().strftime('%Y-%m-%d')}")
        print(f"Age: {student.get_age()}")
        print(f"Sex: {student.get_sex()}")
        print(f"Country of birth: {student.get_country_of_birth()}")
        print()

# takes year attribute from students ,searchs by given input
def show_students_by_year(students):
    year = input("Enter year: ")
    for student in students:
        if student.get_date_of_birth().strftime("%Y") == year:
            print(f"Student number: {student.get_student_number()}")
            print(f"First name: {student.get_first_name()}")
            print(f"Last name: {student.get_last_name()}")
            print(f"Date of birth: {student.get_date_of_birth().strftime('%Y-%m-%d')}")
            print(f"Age: {student.get_age()}")
            print(f"Sex: {student.get_sex()}")
            print(f"Country of birth: {student.get_country_of_birth()}")
            print()

# uses get and setters methods to change student data
def modify_student(students):
    student_number = int(input("Enter student number: "))
    for student in students:
        if student.get_student_number() == student_number:
            field = input("Enter field to modify (1=student number, 2=first name, 3=last name, 4=date of birth, 5=sex, 6=country of birth): ")
            if field == "1":
                new_value = int(input("Enter new student number: "))
                student.set_student_number(new_value)
            elif field == "2":
                new_value = input("Enter new first name: ")
                student.set_first_name(new_value)
            elif field == "3":
                new_value = input("Enter new last name: ")
                student.set_last_name(new_value)
            elif field == "4":
                new_value_str = input("Enter new date of birth (YYYY-MM-DD): ")
                new_value = datetime.datetime.strptime(new_value_str, "%Y-%m-%d").date()
                student.set_date_of_birth(new_value)
            elif field == "5":
                new_value = input("Enter new sex (M/F): ")
                student.set_sex(new_value)
            elif field == "6":
                new_value = input("Enter new country of birth: ")
                student.set_country_of_birth(new_value)
            else:
                print("Invalid field.")
                return
            print("Student record modified.")
            return
    print("Student not found.")


# deleting student by given int input / finds number by searching true students list
def delete_student(students):
    student_number = int(input("Enter student number: "))
    for i in range(len(students)):
        if students[i].get_student_number() == student_number:
            del students[i]
            print("Student deleted.")
            return
    print("Student not found.")

# creates a students list and calls functions
def main():
    students = []
    while True:
        print("Menu:")
        print("1. Write student data to file")
        print("2. Read student data from file")
        print("3. Add new student")
        print("4. Find student by student number")
        print("5. Show all students")
        print("6. Show students born in a given year")
        print("7. Modify student record")
        print("8. Delete student")
        print("9. Quit")
        choice = input("Enter choice: ")
        if choice == "1":
            write_to_file(students)
        elif choice == "2":
            students = read_from_file()
        elif choice == "3":
            add_student(students)
        elif choice == "4":
            find_student(students)
        elif choice == "5":
            show_all_students(students)
        elif choice == "6":
            show_students_by_year(students)
        elif choice == "7":
            modify_student(students)
        elif choice == "8":
            delete_student(students)
        elif choice == "9":
            break
        else:
            print("Invalid choice.")

# calls main function
if __name__ == "__main__":
    main()