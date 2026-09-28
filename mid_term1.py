class StudentDatabase:
                                         #  Class attribute named student_list
    student_list = []

                                         # Class method add_student() holo insert Student instances
    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)


class Student:
                                                                            #Constructor
    # Encapsulation
    def __init__(self, student_id, name, department, is_enrolled=True):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

        # Automatic insert  object into StudentDatabase.student_list
        StudentDatabase.add_student(self)

    # Getters for safe access to private attributes
    @property
    def student_id(self):
        return self.__student_id

    @property
    def name(self):
        return self.__name

    @property
    def department(self):
        return self.__department

    @property
    def is_enrolled(self):
        return self.__is_enrolled

                            # enroll student with error handling for already enrolled state
    def enroll_student(self):
        if self.__is_enrolled:
            print(f"Error: Student '{self.__name}' (ID: {self.__student_id}) is already enrolled.")
        else:
            self.__is_enrolled = True
            print(f"Success: Student '{self.__name}' (ID: {self.__student_id}) has been enrolled successfully.")

                                     # Method to drop student with error handling for not enrolled state
    def drop_student(self):
        if not self.__is_enrolled:
            print(f"Error: Student '{self.__name}' (ID: {self.__student_id}) is not enrolled.")
        else:
            self.__is_enrolled = False
            print(f"Success: Student '{self.__name}' (ID: {self.__student_id}) has dropped out.")

       # Method display student information jonno
    def view_student_info(self):
        status = "Enrolled" if self.__is_enrolled else "Not Enrolled / Dropped"
        print(f"ID: {self.__student_id} | Name: {self.__name:<15} | Department: {self.__department:<10} | Status: {status}")


#           Helper function holo find a student by ID in the StudentDatabase
def find_student_by_id(student_id):
    for student in StudentDatabase.student_list:
        if student.student_id == student_id:
            return student
    return None


#Initializing Sample Student Object
s1 = Student("S101", "Atik Rahman", "CSE", is_enrolled=True)
s2 = Student("S102", "Jhankar Ahmed", "EEE", is_enrolled=True)
s3 = Student("S103", "Nusrat Jahan", "BBA", is_enrolled=False)


#   Menu System ar Error Handling
def main_menu():
    while True:
        print("Student database Management system ")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            print("\n all stu. list")
            if not StudentDatabase.student_list:
                print("No students found in the database.")
            else:
                for student in StudentDatabase.student_list:
                    student.view_student_info()

        elif choice == '2':
            target_id = input("Enter Student ID to Enroll: ").strip()
            student = find_student_by_id(target_id)
            if student:
                student.enroll_student()
            else:
                print(f"Error: Invalid Student ID '{target_id}'. Student not found.")

        elif choice == '3':
            target_id = input("Enter Student ID to Drop: ").strip()
            student = find_student_by_id(target_id)
            if student:
                student.drop_student()
            else:
                print(f"Error: Invalid Student ID '{target_id}'. Student not found.")

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option selected! Please choose between 1 and 4.")

main_menu() # run kori



