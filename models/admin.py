from models.user import User

class Admin(User):
    
    def __init__(self,user_id, first_name,last_name, email, password, adminID, phone, address):
        
        super().__init__(user_id, first_name,last_name, email, password, phone, address)
        
        self.adminID = adminID
        self.students = {}
        self.courses = {}
        self.announcements = []
        self.timetable = {}
        self.books = []
        self.exam_schedule = []
        
    def add_student(self,student):
        if student.student_id in self.students:
            print("Student already Exist")
        else:
            self.students[student.student_id]=student
            print("Student Added Successfully")
    
    def remove_student(self,student):
        if student.student_id in self.students:
            del self.students[student.student_id]
            print("Student removed successfully")
        else :
            print("Student not found ")

    def view_all_students(self):
        for student_id,student in self.students.items():
            print(f"ID : {student_id} Name : {student.first_name} {student.last_name}")

    def view_student_profile(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            print(f"Student ID: {student.student_id}")
            print(f"Name: {student.first_name} {student.last_name}")
            print(f"Email: {student.email}")
            print(f"Phone: {student.phone}")
            print(f"Address: {student.address}")
            print(f"Courses: {student.courses}")
        else:
            print("Student not found")

    def search_student(self,first_name,last_name):
        found=False
        for student in self.students.values():
            if student.first_name==first_name and student.last_name==last_name:
                print(f"Student ID: {student.student_id}")
                print(f"Name: {student.first_name} {student.last_name}")
                print(f"Email: {student.email}")
                print(f"Phone: {student.phone}")
                print(f"Address: {student.address}")
                print(f"Courses: {student.courses}")    
                found=True  
        if not found:
            print("student not found ")   


    def assign_grade(self,student_id,subject,grade):
        if student_id in self.students:
            self.students[student_id].grades[subject]=grade
            print("Grade assigned successfully")
        else :
            print("student not found")

    def update_marks(self,student_id,subject,grade):
        if student_id in self.students:
            if  subject in self.students[student_id].grades:
                self.students[student_id].grades[subject]=grade
                print("Grade updated successfully")
            else:
                print("subject not found")
        else:
            print("student not found")

    def view_student_grades(self,student_id):
        if student_id in self.students:
            print(self.students[student_id].grades)
        else:
            print("student not found ")
    
    def mark_attendance(self,student_id,subject,classes_held,classed_attended):
        if student_id in self.students:
            self.students[student_id].attendance[subject]=[classes_held,classed_attended]
            print("Attendance marked successfully")
        else:
            print("student not found")
    
    def view_student_attendance(self,student_id):
        if student_id in self.students:
            print(self.students[student_id].attendance)
        else:
            print("student not found")

    def update_fee_status(self,student_id,semester,status):
        if student_id in self.students:
            if semester in self.students[student_id].fee:
                self.students[student_id].fees[semester] = status
                print("status updated successfully")
            else:
                print("semester not found ")
        else:
            print("student not found ")



    def view_all_fees(self,student_id):
        if student_id in self.students:
            print(self.students[student_id].fees)
        else:
            print("student not found ")

    def add_course(self,course_name):
        if course_name not in self.courses:
            self.courses[course_name]={}
            print(f"{course_name} added successfully")
        else:
            print("Course already exist")

    def remove_course(self,course_name):
        if course_name in self.courses:
            del self.courses[course_name]
            print(f"{course_name} removed successfully")
        else:
            print("course not found")
    
    def view_all_courses(self):
        print(self.courses)

    def assign_course_material(self,course_name,material):
        if course_name in self.courses:
            self.courses[course_name]=material
            print(f"Material assigned to {course_name} successfully")
        else:
            print(f"{course_name} not found ")
    

    def enroll_student_in_course(self,student_id,course_name):
        if student_id in self.students:
            if course_name in self.courses:
                if course_name in self.students[student_id].courses:
                    print("already enrolled")
                else:
                    self.students[student_id].courses.append(course_name)
                    print(f"Student enrolled successfully")
            else:
                print(f"course not found")
        else:
            print("student not found")

    def make_announcement(self,announcement):
        self.announcements.append(announcement)
        print("announcement made successfully")
    

    def delete_annoumcenent(self,announcement):
        if announcement in self.announcements:
            self.announcements.remove(announcement)
            print("announcement removed successfully")
        else:
            print("announcement not found")
    

    def view_all_announcements(self):
        print(self.announcements)

    def schedule_exam(self,exam_name,exam_date):
        self.exam_schedule.append({"Exam : ":exam_name,"Date :" :exam_date})
        print("exam scheduled successfully")

    def update_exam_schedule(self,exam_name,new_date):
        found=False
        for exam in self.exam_schedule:
            if exam["exam"] == exam_name:
                exam["date"]=new_date
                print("date updated successfully")
                found=True
        if not found:
            print("exam not scheduled")


    def update_timetable(self,day,schedule):
        self.timetable.update({day:schedule})
        print("timetable updated successfully")


    def view_timetable(self):
        print(self.timetable)

    def add_book(self,book_name):
        if book_name in self.books:
            print("book already there")
        else:
            self.books.append(book_name)
            print(f"{book_name} successfully added ")
    


    def remove_book(self,book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"{book_name} successfully removed ")
        else:
            print("book not found")

    
    def view_all_books(self):
        print(self.books)

    def send_notification(self,student_id,message):
        if student_id in self.students:
            self.students[student_id].notifications.append(message)
            print("notification added successfully")
        else:
            print("student not found")
        
    def generate_student_report(self,student_id):
        if student_id in self.students:
            student = self.students[student_id]
            print("========== Student Report ==========")
            print(f"Student ID: {student.student_id}")
            print(f"Name: {student.first_name} {student.last_name}")
            print(f"Email: {student.email}")
            print(f"Phone: {student.phone}")
            print(f"Age: {student.age}")
            print(f"Gender: {student.gender}")
            print(f"Department: {student.department}")
            print("---------- Academic Info ----------")
            print(f"Grade: {student.grade}")
            print(f"Midterm Score: {student.midterm_score}")
            print(f"Final Score: {student.final_score}")
            print(f"Total Score: {student.total_score}")
            print(f"Assignments Avg: {student.assignments_avg}")
            print(f"Quizzes Avg: {student.quizzes_avg}")
            print(f"Participation Score: {student.participation_score}")
            print(f"Projects Score: {student.projects_score}")
            print("---------- Attendance ----------")
            print(f"Attendance: {student.attendance}")
            print("---------- Courses ----------")
            print(f"Courses: {student.courses}")
            print("---------- Fees ----------")
            print(f"Fees: {student.fees}")
            print("====================================")
        else:
            print("Student not found")
                