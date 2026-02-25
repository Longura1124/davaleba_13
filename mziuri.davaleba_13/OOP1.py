class Student:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def get_info(self):
        print(f"სტუდენტი: {self.firstname} {self.lastname}")


class School:
    def __init__(self, school_name, school_adress):
        self.school_name = school_name
        self.school_adress = school_adress
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        if 1 <= index <= len(self.students):
            self.students.pop(index - 1)
        else:
            print("არასწორი ინდექსი!")

    def show_students(self):
        print(f"\nსკოლა: {self.school_name}")
        print("სტუდენტები:")
        for student in self.students:
            student.get_info()


school = School("თბილისის 112-ე საჯარო სკოლა", "თბილისი, დადიანის ქუჩა")

student1 = Student("ნიკა", "ლონგურაშვილი", 16)
student2 = Student("ნიკა", "ჩორგოლიანი", 17)
student3 = Student("ნიკა", "კაპანაძე", 16)
student4 = Student("ნიკა", "პაიჭაძე", 16)

school.add_student(student1)
school.add_student(student2)
school.add_student(student3)

school.show_students()

school.remove_student(5)
school.remove_student(2)

print("\nწაშლის შემდეგ:")
school.show_students()