import numpy as np
import pandas as pd

class Analytics:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)

    # ========== STUDENT PERFORMANCE ANALYSIS ==========

    def average_midterm_score(self):
        avg = np.mean(self.df['Midterm_Score'])
        print(f"Average Midterm Score: {round(avg, 2)}")

    def average_final_score(self):
        avg = np.mean(self.df['Final_Score'])
        print(f"Average Final Score: {round(avg, 2)}")

    def average_attendance(self):
        avg = np.mean(self.df['Attendance (%)'])
        print(f"Average Attendance: {round(avg, 2)}%")

    def average_total_score(self):
        avg = np.mean(self.df['Total_Score'])
        print(f"Average Total Score: {round(avg, 2)}")

    def highest_scoring_student(self):
        idx = np.argmax(self.df['Total_Score'])
        student = self.df.iloc[idx]
        print(f"Highest Scoring Student:")
        print(f"  Name: {student['First_Name']} {student['Last_Name']}")
        print(f"  ID: {student['Student_ID']}")
        print(f"  Total Score: {student['Total_Score']}")
        print(f"  Grade: {student['Grade']}")

    def lowest_scoring_student(self):
        idx = np.argmin(self.df['Total_Score'])
        student = self.df.iloc[idx]
        print(f"Lowest Scoring Student:")
        print(f"  Name: {student['First_Name']} {student['Last_Name']}")
        print(f"  ID: {student['Student_ID']}")
        print(f"  Total Score: {student['Total_Score']}")
        print(f"  Grade: {student['Grade']}")

    def average_cgpa(self):
        avg = np.mean(self.df['Total_Score']) / 25
        print(f"Average CGPA: {round(avg, 2)}")

    def score_std_deviation(self):
        std = np.std(self.df['Total_Score'])
        print(f"Score Standard Deviation: {round(std, 2)}")

    def passing_students_count(self):
        passing = np.sum(self.df['Grade'] != 'F')
        total = len(self.df)
        print(f"Passing Students: {passing} out of {total}")
        print(f"Pass Rate: {round((passing/total)*100, 2)}%")

    def failing_students_count(self):
        failing = np.sum(self.df['Grade'] == 'F')
        total = len(self.df)
        print(f"Failing Students: {failing} out of {total}")
        print(f"Fail Rate: {round((failing/total)*100, 2)}%")

    # ========== DEPARTMENT WISE ANALYSIS ==========

    def department_average_scores(self):
        print("Department wise Average Total Score:")
        departments = self.df['Department'].unique()
        for dept in departments:
            dept_df = self.df[self.df['Department'] == dept]
            avg = np.mean(dept_df['Total_Score'])
            print(f"  {dept}: {round(avg, 2)}")

    def best_department(self):
        departments = self.df['Department'].unique()
        best = None
        best_avg = 0
        for dept in departments:
            dept_df = self.df[self.df['Department'] == dept]
            avg = np.mean(dept_df['Total_Score'])
            if avg > best_avg:
                best_avg = avg
                best = dept
        print(f"Best Performing Department: {best} with avg score {round(best_avg, 2)}")

    def department_attendance(self):
        print("Department wise Average Attendance:")
        departments = self.df['Department'].unique()
        for dept in departments:
            dept_df = self.df[self.df['Department'] == dept]
            avg = np.mean(dept_df['Attendance (%)'])
            print(f"  {dept}: {round(avg, 2)}%")

    # ========== OTHER ANALYSIS ==========

    def average_study_hours(self):
        avg = np.mean(self.df['Study_Hours_per_Week'])
        print(f"Average Study Hours Per Week: {round(avg, 2)}")

    def average_stress_level(self):
        avg = np.mean(self.df['Stress_Level (1-10)'])
        print(f"Average Stress Level: {round(avg, 2)} / 10")

    def average_sleep_hours(self):
        avg = np.mean(self.df['Sleep_Hours_per_Night'])
        print(f"Average Sleep Hours Per Night: {round(avg, 2)}")

    def sleep_vs_grades(self):
        correlation = np.corrcoef(self.df['Sleep_Hours_per_Night'], self.df['Total_Score'])[0, 1]
        print(f"Correlation between Sleep Hours and Total Score: {round(correlation, 2)}")
        if correlation > 0:
            print("More sleep → Better grades!")
        else:
            print("Sleep hours don't strongly impact grades in this dataset!")

    def study_hours_vs_grades(self):
        correlation = np.corrcoef(self.df['Study_Hours_per_Week'], self.df['Total_Score'])[0, 1]
        print(f"Correlation between Study Hours and Total Score: {round(correlation, 2)}")
        if correlation > 0:
            print("More study hours → Better grades!")
        else:
            print("Study hours don't strongly impact grades in this dataset!")

    def stress_vs_grades(self):
        correlation = np.corrcoef(self.df['Stress_Level (1-10)'], self.df['Total_Score'])[0, 1]
        print(f"Correlation between Stress Level and Total Score: {round(correlation, 2)}")
        if correlation < 0:
            print("Higher stress → Lower grades!")
        else:
            print("Stress doesn't strongly impact grades in this dataset!")

    def grade_distribution(self):
        print("Grade Distribution:")
        grades = ['A', 'B', 'C', 'D', 'F']
        for grade in grades:
            count = np.sum(self.df['Grade'] == grade)
            percentage = round((count / len(self.df)) * 100, 2)
            print(f"  {grade}: {count} students ({percentage}%)")

    def internet_access_impact(self):
        with_internet = self.df[self.df['Internet_Access_at_Home'] == 'Yes']['Total_Score']
        without_internet = self.df[self.df['Internet_Access_at_Home'] == 'No']['Total_Score']
        print(f"Average Score with Internet Access: {round(np.mean(with_internet), 2)}")
        print(f"Average Score without Internet Access: {round(np.mean(without_internet), 2)}")

    def extracurricular_impact(self):
        with_extra = self.df[self.df['Extracurricular_Activities'] == 'Yes']['Total_Score']
        without_extra = self.df[self.df['Extracurricular_Activities'] == 'No']['Total_Score']
        print(f"Average Score with Extracurricular Activities: {round(np.mean(with_extra), 2)}")
        print(f"Average Score without Extracurricular Activities: {round(np.mean(without_extra), 2)}")

    def run_full_report(self):
        print("=" * 50)
        print("        STUDENT PORTAL ANALYTICS REPORT")
        print("=" * 50)
        print("\n--- Student Performance ---")
        self.average_midterm_score()
        self.average_final_score()
        self.average_attendance()
        self.average_total_score()
        self.average_cgpa()
        self.score_std_deviation()
        self.passing_students_count()
        self.failing_students_count()
        print("\n--- Top & Bottom Students ---")
        self.highest_scoring_student()
        self.lowest_scoring_student()
        print("\n--- Department Analysis ---")
        self.department_average_scores()
        self.best_department()
        self.department_attendance()
        print("\n--- Lifestyle Analysis ---")
        self.average_study_hours()
        self.average_stress_level()
        self.average_sleep_hours()
        self.sleep_vs_grades()
        self.study_hours_vs_grades()
        self.stress_vs_grades()
        print("\n--- Grade Distribution ---")
        self.grade_distribution()
        print("\n--- Impact Analysis ---")
        self.internet_access_impact()
        self.extracurricular_impact()
        print("\n" + "=" * 50)

