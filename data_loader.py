import pandas as pd
from models.students import Student
from models.admin import Admin

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def create_students(df):
    students = []
    for _, row in df.iterrows():
        student = Student(
            user_id=row['Student_ID'],
            first_name=row['First_Name'],
            last_name=row['Last_Name'],
            email=row['Email'],
            password=row['Password'],
            student_id=row['Student_ID'],
            phone=row['Phone'],
            address=row['Address'],
            age=row['Age'],
            gender=row['Gender'],
            department=row['Department']
        )
        # Fill extra attributes from dataset
        student.midterm_score = row['Midterm_Score']
        student.final_score = row['Final_Score']
        student.assignments_avg = row['Assignments_Avg']
        student.quizzes_avg = row['Quizzes_Avg']
        student.participation_score = row['Participation_Score']
        student.projects_score = row['Projects_Score']
        student.total_score = row['Total_Score']
        student.grade = row['Grade']
        student.attendance = row['Attendance (%)']
        student.study_hours_per_week = row['Study_Hours_per_Week']
        student.extracurricular_activities = row['Extracurricular_Activities']
        student.internet_access_at_home = row['Internet_Access_at_Home']
        student.parent_education_level = row['Parent_Education_Level']
        student.family_income_level = row['Family_Income_Level']
        student.stress_level = row['Stress_Level (1-10)']
        student.sleep_hours_per_night = row['Sleep_Hours_per_Night']
        student.fee_status = row['Fee_Status']

        # Load grades into dictionary
        student.grades = {
            'Midterm': row['Midterm_Score'],
            'Final': row['Final_Score'],
            'Assignments': row['Assignments_Avg'],
            'Quizzes': row['Quizzes_Avg'],
            'Participation': row['Participation_Score'],
            'Projects': row['Projects_Score'],
        }

        # Load courses into list
        if row['Courses_Enrolled'] != 'None':
            student.courses = [c.strip() for c in str(row['Courses_Enrolled']).split(',')]
        else:
            student.courses = []

        # Load timetable
        if row['Courses_Enrolled'] != 'None':
            courses = [c.strip() for c in str(row['Courses_Enrolled']).split(',')]
            student.timetable = {
                "Monday": courses[0] if len(courses) > 0 else "",
                "Tuesday": courses[1] if len(courses) > 1 else "",
                "Wednesday": courses[2] if len(courses) > 2 else "",
                "Thursday": courses[3] if len(courses) > 3 else "",
            }
        else:
            student.timetable = {}

        # Load notifications
        if row['Notifications'] != 'None':
            student.notifications = [n.strip() for n in str(row['Notifications']).split(',')]
        else:
            student.notifications = []

        students.append(student)
    return students

def setup_portal(filepath):
    # Step 1: Load the CSV
    df = load_data(filepath)

    # Step 2: Create all student objects
    students = create_students(df)  

    # Step 3: Create admin
    admin = Admin(
        user_id="A01",
        first_name="Super",
        last_name="Admin",
        email="admin@portal.com",
        password="admin123",
        adminID="AD01",
        phone="07000000000",
        address="Admin Office, London"
    )

    # Step 4: Add all students silently
    for student in students:
        admin.students[student.student_id] = student

    print(f"Portal ready! {len(students)} students loaded successfully!")
    return admin