# ---------------------------
# Base Class: Person
# ---------------------------
class Person:
    def __init__(self, person_id, name, email):
        self.id = person_id
        self.name = name
        self.__email = email  # Private attribute

    # Display basic info
    def display_info(self):
        return f"ID: {self.id}, Name: {self.name}, Email: {self.__email}"

    # Getter for email
    def get_email(self):
        return self.__email


# ---------------------------
# Subclass: Student
# ---------------------------
class Student(Person):
    def __init__(self, person_id, name, email, major, gpa):
        super().__init__(person_id, name, email)
        self.major = major
        self.gpa = gpa
        self.courses = []

    # Enroll in a course
    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} enrolled in {course}")
        else:
            print(f"{self.name} is already enrolled in {course}")

    # Compare students by GPA
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.gpa < other.gpa
        return NotImplemented

    # Debug representation
    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}', gpa={self.gpa})"


# ---------------------------
# Subclass: Professor
# ---------------------------
class Professor(Person):
    def __init__(self, person_id, name, email, department):
        super().__init__(person_id, name, email)
        self.department = department
        self.courses_teaching = []

    # Assign course
    def assign_course(self, course):
        if course not in self.courses_teaching:
            self.courses_teaching.append(course)
            print(f"{self.name} is now teaching {course}")
        else:
            print(f"{self.name} already teaches {course}")


# ---------------------------
# Example Usage
# ---------------------------
if __name__ == "__main__":
    # Create Students
    s1 = Student(1, "Alice", "alice@example.com", "Computer Science", 3.8)
    s2 = Student(2, "Bob", "bob@example.com", "Mathematics", 3.5)

    # Create Professor
    p1 = Professor(101, "Dr. Smith", "smith@example.com", "Physics")

    # Enroll students in courses
    s1.enroll("CS101")
    s2.enroll("MATH201")

    # Assign professor courses
    p1.assign_course("PHYS101")

    # Compare students by GPA
    print(s1 < s2)  # False, because 3.8 > 3.5

    # Display info
    print(s1.display_info())
    print(p1.display_info())

    # Debug output
    print(repr(s1))
    print(repr(s2))
