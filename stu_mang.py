# student_management.py

# Import required modules
import json


class Student:
    """Class to store and manage student details."""

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_info(self):
        """Display student's inforation."""
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")


class StudentManager:
    """Class to manage multiple students."""

    def add_student(self):
        """Add a new student to the list."""
        roll_no = input("Enter roll number: ")
        name = input("Enter student's name: ")
        marks = float(input("Enter marks: "))
        new_student = Student(name, roll_no, marks)
        self.students.append(new_student)
        print(f"Student '{name}' added successfully!\n")

    def __init__(self):
        self.students = []

    def display_students(self):

        """Display all students."""
        if not self.students:
            print("No student records available.\n")
            return
        print("\n---- Student List ----")
        for student in self.students:
            student.display_info()
        print("----------------------\n")

    def save_to_file(self, filename):
        """Save all student data to a JSON file."""
        data = []
        for student in self.students:
            data.append({
                'name': student.name,
                'roll_no': student.roll_no,
                'marks': student.marks
            })
        with open(filename, 'w') as file:
            json.dump(data, file)
        print(f"Data saved successfully to '{filename}'!\n")

    def count_students(self):
        """Count and display total number of students."""
        total = len(self.students)
        print(f"\nTotal number of students: {total}\n")

    def load_from_file(self, filename):
        """Load student data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            self.students = []
            for item in data:
                loaded_student = Student(item['name'], item['roll_no'], item['marks'])
                self.students.append(loaded_student)
            print(f"Data loaded successfully from '{filename}'!\n")
        except FileNotFoundError:
            print(f"File '{filename}' not found.\n")


def show_menu():
    """Display the main menu."""
    print("=== Student Management System ===")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Save to File")
    print("4. Load from File")
    print("5. Count Students")
    print("6. Exit")

def main():
    """Main function to run the program."""
    manager = StudentManager()
    filename = "students.json"

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            manager.add_student()
            pass
        elif choice == '2':
            manager.display_students()
        elif choice == '3':
            manager.save_to_file(filename)
        elif choice == '4':
            manager.load_from_file(filename)
        elif choice == '5':
            manager.count_students()
        elif choice == '6':
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the program
if __name__ == "__main__":
    main()
