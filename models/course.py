class Course:

    def __init__(self, course_name, course_code, instructor, credits):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.credits = credits
        self.course_material = []
        self.students_enrolled = []


    def get_course_details(self):
        print(f"Course_Name : {self.course_name}")
        print(f"Course_Code : {self.course_code}")
        print(f"Course_Instructor : {self.instructor}")
        print(f"Total_Credits : {self.credits}")

    def add_material(self,material):
        if material in self.course_material:
            print("material already exist")
        else:
            self.course_material.append(material)
            print("material added successfully")


    def remove_material(self,material):
        if material in self.course_material:
            self.course_material.remove(material)
            print("material removed successfully")#
        else:
            print("material not found ")

    def view_material(self):
        print(self.course_material)
    


    def add_student(self,student_id):
        if student_id in self.students_enrolled:
            print("already enrolled")
        else:
            self.students_enrolled.append(student_id)
            print(f"{student_id} enrolled successfully")

    def remove_student(self,student_id):
        if student_id in self.students_enrolled:
            self.students_enrolled.remove(student_id)
            print(f"{student_id} removed successfully")
        else:
            print("student not found")
    

    def update_instructor(self,new_instructor):
        self.instructor=new_instructor
        print("instructor updated successfully")
        