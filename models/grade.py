class Grade:
    def __init__(self, student_id, course_name, midterm_score, final_score, assignments_avg, quizzes_avg, participation_score, projects_score, total_score, grade):
        self.student_id = student_id
        self.course_name = course_name
        self.midterm_score = midterm_score
        self.final_score = final_score
        self.assignments_avg = assignments_avg
        self.quizzes_avg = quizzes_avg
        self.participation_score = participation_score
        self.projects_score = projects_score
        self.total_score = total_score
        self.grade = grade

    def get_grade_details(self):
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course_name}")
        print(f"Midterm Score: {self.midterm_score}")
        print(f"Final Score: {self.final_score}")
        print(f"Assignments Avg: {self.assignments_avg}")
        print(f"Quizzes Avg: {self.quizzes_avg}")
        print(f"Participation Score: {self.participation_score}")
        print(f"Projects Score: {self.projects_score}")
        print(f"Total Score: {self.total_score}")
        print(f"Grade: {self.grade}")
    

    def update_midterm_score(self, new_score):
        self.midterm_score = new_score
        print("Midterm score updated successfully")

    def update_final_score(self, new_score):
        self.final_score = new_score
        print("Final score updated successfully")

    def update_assignments_avg(self, new_avg):
        self.assignments_avg = new_avg
        print("Assignments average updated successfully")

    def update_quizzes_avg(self, new_avg):
        self.quizzes_avg = new_avg
        print("Quizzes average updated successfully")

    def update_participation_score(self, new_score):
        self.participation_score = new_score
        print("Participation score updated successfully")

    def update_projects_score(self, new_score):
        self.projects_score = new_score
        print("Projects score updated successfully")


    def calculate_total_score(self):
        self.total_score=(self.midterm_score*0.25)+(self.final_score*0.35)+(self.assignments_avg*0.15)+(self.quizzes_avg*0.10)+(self.projects_score*0.10)+(self.participation_score*0.05)
        print(self.total_score)

    def assign_letter_grade(self):
        if self.total_score >= 90:
            self.grade = "A"
        elif self.total_score >= 80:
            self.grade = "B"
        elif self.total_score >= 70:
            self.grade = "C"
        elif self.total_score >= 60:
            self.grade = "D"
        else:
            self.grade = "F"
        print(f"Grade assigned: {self.grade}")