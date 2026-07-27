from models.user import User

class Student(User):

    def __init__(self, user_id, first_name, last_name, email, password, student_id, phone, address, age, gender, department):
        super().__init__(user_id, first_name, last_name, email, password, phone, address)
        self.student_id = student_id
        self.age = age
        self.gender = gender
        self.department = department
        self.courses = []
        self.grades = {}
        self.attendance = {}
        self.fees = {}
        self.borrowed_books = []
        self.exam_schedule = []
        self.course_materials = {}
        self.cgpa_progress = []
        self.midterm_score = 0
        self.final_score = 0
        self.assignments_avg = 0
        self.quizzes_avg = 0
        self.participation_score = 0
        self.projects_score = 0
        self.total_score = 0
        self.grade = ""
        self.study_hours_per_week = 0
        self.extracurricular_activities = ""
        self.internet_access_at_home = ""
        self.parent_education_level = ""
        self.family_income_level = ""
        self.stress_level = 0
        self.sleep_hours_per_night = 0

    def enroll_course(self,course_name):
        if course_name in self.courses:
            print("Already Enrolled")
        else:
            self.courses.append(course_name)
            print(f"{course_name} Enrolled Successfully")

    def drop_course(self,course_name):
        if course_name in self.courses:
            self.courses.remove(course_name)
            print(f"{course_name} dropped successfully!")
        else:
            print("You are not enrolled in this course")

    def view_courses(self):
        print (self.courses)

    def view_grades(self):
        print(self.grades)

    def view_gpa(self):
        total=0
        if len(self.grades)==0:
            print("No grades available yet")
            return
        get_point={"A":10,"B":8,"C":6,"D":4,"F":0}
        for check in self.grades.values():
            value=get_point.get(check)
            total=(total+value)
        cgpa=total/len(self.grades)
        print (f"Your CGPA For This Semester Is {cgpa}")
    
    def view_attendance(self):
        print(self.attendance)
    

    def view_attendance_percentage(self):
        for subject,check in self.attendance.items():
            classes_held=check[0]
            classes_attended=check[1]
            percentage=(classes_attended/classes_held)*100
            print(f"{subject} : {percentage}")

    def view_announcement(self,announcement):
        print(announcement)

    def view_timetable(self,timetable):
        print(timetable)
    def view_profile(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Department: {self.department}")
        print(f"Courses Enrolled: {self.courses}")

    def view_result(self):
        for subject,check in self.grades.items():
            print(f"{subject} : {check}")

    def view_grade_by_subject(self,subject_name):
        if subject_name in self.grades:
            print(f"{subject_name} : {self.grades[subject_name]}")
        else: 
            print("subject not found")
    def view_cgpa_progress(self):
        for index,cgpa in enumerate(self.cgpa_progress):
            print(f"Semester {index+1 } : {cgpa}")

    def view_fee_status(self):
        for sem,status in self.fees.items():
            print(f"{sem} : {status}" )

    def pay_fee(self,check_status):
        if check_status in self.fees:
            if self.fees[check_status]=="Pending":
                self.fees[check_status]="Paid"
                print("fee paid successfully")
            elif self.fees[check_status]=="Paid":
                print("Already Paid")
        else:
            print("semester not found") 

    def borrow_book(self,book_name):
        if book_name in self.borrowed_books:
            print("Already borrowed")
        else:
            self.borrowed_books.append(book_name)
            print("Success")     
 
    def return_book(self,book_name):
        if book_name in self.borrowed_books:
            self.borrowed_books.remove(book_name)
            print("book returned successfully")
        else: 
            print("book not found")   

    def view_borrowed_books(self):
        print(self.borrowed_books)

    def view_notifications(self):
        print(self.notifications)

    def mark_notification_read(self,check_status):
        if check_status in self.notifications:
            self.notifications.remove(check_status)
            print("marked as read")
        else:
            print("notification not found")

    def view_exam_schedule(self):
        print(self.exam_schedule)
    
    def view_admit_card(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Courses: {self.courses}")
        print(f"Exam Schedule: {self.exam_schedule}")

    def  view_course_details(self,course_name):
        if course_name in self.courses:
            print(self.course_materials[course_name])
        else:
            print("course not found")

             
    def view_course_material(self):
        print(self.course_materials)
    
    def view_midterm_score(self):
        print(f"Midterm Score: {self.midterm_score}")

    def view_final_score(self):
        print(f"Final Score: {self.final_score}")

    def view_assignments_avg(self):
        print(f"Assignments Average: {self.assignments_avg}")

    def view_quizzes_avg(self):
        print(f"Quizzes Average: {self.quizzes_avg}")

    def view_participation_score(self):
        print(f"Participation Score: {self.participation_score}")

    def view_projects_score(self):
        print(f"Projects Score: {self.projects_score}")

    def view_total_score(self):
        print(f"Total Score: {self.total_score}")

    def view_gender(self):
        print(f"Gender: {self.gender}")

    def view_age(self):
        print(f"Age: {self.age}")

    def view_department(self):
        print(f"Department: {self.department}")
        
    def view_grade(self):
        print(f"Grade : {self.grade}")

    def view_study_hours(self):
        print(f"Study Hours Per Week: {self.study_hours_per_week}")

    def view_extracurricular_activities(self):
        print(f"Extracurricular Activities: {self.extracurricular_activities}")

    def view_internet_access(self):
        print(f"Internet Access at Home: {self.internet_access_at_home}")

    def view_parent_education(self):
        print(f"Parent Education Level: {self.parent_education_level}")

    def view_family_income(self):
        print(f"Family Income Level: {self.family_income_level}")

    def view_stress_level(self):
        print(f"Stress Level: {self.stress_level}")

    def view_sleep_hours(self):
        print(f"Sleep Hours Per Night: {self.sleep_hours_per_night}")