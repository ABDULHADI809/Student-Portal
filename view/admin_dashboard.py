import tkinter as tk
from tkinter import messagebox, simpledialog
from analytics import Analytics

class AdminDashboard:
    def __init__(self, root, admin):
        self.root = root
        self.admin = admin
        self.analytics = Analytics("data/Students_Performance_Dataset_Updated.csv")
        self.root.title("Student Portal - Admin Dashboard")
        self.root.geometry("1100x680")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)

        self.build_ui()

    def build_ui(self):
        # ===== SIDEBAR =====
        sidebar = tk.Frame(self.root, bg="#181825", width=220)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        tk.Label(
            sidebar,
            text="Admin Panel",
            font=("Arial", 16, "bold"),
            bg="#181825",
            fg="#cdd6f4"
        ).pack(pady=(30, 5))

        tk.Label(
            sidebar,
            text="Super Admin",
            font=("Arial", 10),
            bg="#181825",
            fg="#6c7086"
        ).pack(pady=(0, 30))

        sections = [
            ("🏠  Dashboard", self.show_dashboard),
            ("👥  All Students", self.show_all_students),
            ("🔍  Search Student", self.search_student),
            ("📊  Analytics", self.show_analytics),
            ("📝  Assign Grade", self.assign_grade),
            ("📅  Mark Attendance", self.mark_attendance),
            ("📢  Send Notification", self.send_notification),
            ("📋  Student Report", self.student_report),
            ("🚪  Logout", self.logout),
        ]

        for name, command in sections:
            btn = tk.Button(
                sidebar,
                text=name,
                font=("Arial", 11),
                bg="#181825",
                fg="#cdd6f4",
                relief="flat",
                anchor="w",
                padx=20,
                cursor="hand2",
                command=command
            )
            btn.pack(fill="x", pady=2)

        # ===== MAIN CONTENT AREA =====
        self.main_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.main_frame.pack(side="right", fill="both", expand=True)

        self.show_dashboard()

    def clear_main(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_main()

        tk.Label(
            self.main_frame,
            text="Welcome, Admin! 👋",
            font=("Arial", 22, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=30, pady=(30, 5))

        tk.Label(
            self.main_frame,
            text="Here's your portal summary",
            font=("Arial", 12),
            bg="#1e1e2e",
            fg="#6c7086"
        ).pack(anchor="w", padx=30, pady=(0, 30))

        # Stats cards
        cards_frame = tk.Frame(self.main_frame, bg="#1e1e2e")
        cards_frame.pack(padx=30, fill="x")

        import numpy as np
        df = self.analytics.df

        cards = [
            ("Total Students", str(len(self.admin.students)), "#89b4fa"),
            ("Avg Total Score", str(round(float(np.mean(df['Total_Score'])), 2)), "#a6e3a1"),
            ("Avg Attendance", str(round(float(np.mean(df['Attendance (%)'])), 2)) + "%", "#fab387"),
            ("Pass Rate", str(round(float(np.sum(df['Grade'] != 'F') / len(df) * 100), 2)) + "%", "#cba6f7"),
        ]

        for title, value, color in cards:
            card = tk.Frame(cards_frame, bg="#313244", width=170, height=100)
            card.pack(side="left", padx=10, pady=10)
            card.pack_propagate(False)

            tk.Label(
                card,
                text=value,
                font=("Arial", 16, "bold"),
                bg="#313244",
                fg=color
            ).pack(pady=(15, 5))

            tk.Label(
                card,
                text=title,
                font=("Arial", 10),
                bg="#313244",
                fg="#6c7086"
            ).pack()

        # Grade distribution
        tk.Label(
            self.main_frame,
            text="Grade Distribution",
            font=("Arial", 16, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=30, pady=(30, 10))

        grades = ['A', 'B', 'C', 'D', 'F']
        colors = ["#a6e3a1", "#89b4fa", "#fab387", "#f9e2af", "#f38ba8"]

        for grade, color in zip(grades, colors):
            import numpy as np
            count = int(np.sum(df['Grade'] == grade))
            percentage = round(count / len(df) * 100, 2)

            row = tk.Frame(self.main_frame, bg="#313244")
            row.pack(fill="x", padx=30, pady=3)

            tk.Label(
                row,
                text=f"Grade {grade}",
                font=("Arial", 11),
                bg="#313244",
                fg=color,
                width=10,
                anchor="w"
            ).pack(side="left", padx=15, pady=8)

            tk.Label(
                row,
                text=f"{count} students ({percentage}%)",
                font=("Arial", 11),
                bg="#313244",
                fg="#cdd6f4"
            ).pack(side="left", padx=15)

    def show_all_students(self):
        self.clear_main()

        tk.Label(
            self.main_frame,
            text="All Students",
            font=("Arial", 22, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=30, pady=(30, 20))

        # Scrollable frame
        canvas = tk.Canvas(self.main_frame, bg="#1e1e2e", highlightthickness=0)
        scrollbar = tk.Scrollbar(self.main_frame, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#1e1e2e")

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True, padx=30)
        scrollbar.pack(side="right", fill="y")

        # Header
        header = tk.Frame(scroll_frame, bg="#313244")
        header.pack(fill="x", pady=2)

        for col, width in [("Student ID", 12), ("Name", 20), ("Department", 15), ("Grade", 8), ("Score", 10)]:
            tk.Label(
                header,
                text=col,
                font=("Arial", 11, "bold"),
                bg="#313244",
                fg="#89b4fa",
                width=width,
                anchor="w"
            ).pack(side="left", padx=10, pady=8)

        # Student rows
        for student in list(self.admin.students.values())[:100]:
            row = tk.Frame(scroll_frame, bg="#1e1e2e")
            row.pack(fill="x", pady=1)

            for value, width in [
                (student.student_id, 12),
                (f"{student.first_name} {student.last_name}", 20),
                (student.department, 15),
                (student.grade, 8),
                (str(student.total_score), 10)
            ]:
                tk.Label(
                    row,
                    text=value,
                    font=("Arial", 10),
                    bg="#1e1e2e",
                    fg="#cdd6f4",
                    width=width,
                    anchor="w"
                ).pack(side="left", padx=10, pady=5)

    def search_student(self):
        self.clear_main()

        tk.Label(
            self.main_frame,
            text="Search Student",
            font=("Arial", 22, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=30, pady=(30, 20))

        # Search by ID
        search_frame = tk.Frame(self.main_frame, bg="#1e1e2e")
        search_frame.pack(anchor="w", padx=30, pady=10)

        tk.Label(
            search_frame,
            text="Enter Student ID:",
            font=("Arial", 12),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(side="left", padx=(0, 10))

        self.search_entry = tk.Entry(
            search_frame,
            font=("Arial", 12),
            bg="#313244",
            fg="#cdd6f4",
            insertbackground="#cdd6f4",
            relief="flat",
            width=20
        )
        self.search_entry.pack(side="left", ipady=6)

        tk.Button(
            search_frame,
            text="Search",
            font=("Arial", 11, "bold"),
            bg="#89b4fa",
            fg="#1e1e2e",
            relief="flat",
            cursor="hand2",
            command=self.do_search
        ).pack(side="left", padx=10, ipady=6, ipadx=10)

        self.result_frame = tk.Frame(self.main_frame, bg="#1e1e2e")
        self.result_frame.pack(fill="x", padx=30, pady=20)

    def do_search(self):
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        student_id = self.search_entry.get().strip()

        if student_id in self.admin.students:
            student = self.admin.students[student_id]
            details = [
                ("Student ID", student.student_id),
                ("Full Name", f"{student.first_name} {student.last_name}"),
                ("Email", student.email),
                ("Phone", student.phone),
                ("Department", student.department),
                ("Grade", student.grade),
                ("Total Score", student.total_score),
                ("Attendance", f"{student.attendance}%"),
            ]

            for label, value in details:
                row = tk.Frame(self.result_frame, bg="#313244")
                row.pack(fill="x", pady=3)

                tk.Label(
                    row,
                    text=label,
                    font=("Arial", 11),
                    bg="#313244",
                    fg="#6c7086",
                    width=15,
                    anchor="w"
                ).pack(side="left", padx=15, pady=10)

                tk.Label(
                    row,
                    text=str(value),
                    font=("Arial", 11),
                    bg="#313244",
                    fg="#cdd6f4",
                    anchor="w"
                ).pack(side="left", padx=15)
        else:
            tk.Label(
                self.result_frame,
                text="Student not found!",
                font=("Arial", 12),
                bg="#1e1e2e",
                fg="#f38ba8"
            ).pack(pady=20)

    def show_analytics(self):
        self.clear_main()

        tk.Label(
            self.main_frame,
            text="Analytics Report",
            font=("Arial", 22, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=30, pady=(30, 20))

        # Scrollable frame
        canvas = tk.Canvas(self.main_frame, bg="#1e1e2e", highlightthickness=0)
        scrollbar = tk.Scrollbar(self.main_frame, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#1e1e2e")

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True, padx=30)
        scrollbar.pack(side="right", fill="y")

        import numpy as np
        df = self.analytics.df

        analytics_data = [
            ("Average Midterm Score", round(float(np.mean(df['Midterm_Score'])), 2)),
            ("Average Final Score", round(float(np.mean(df['Final_Score'])), 2)),
            ("Average Attendance", str(round(float(np.mean(df['Attendance (%)'])), 2)) + "%"),
            ("Average Total Score", round(float(np.mean(df['Total_Score'])), 2)),
            ("Average CGPA", round(float(np.mean(df['Total_Score'])) / 25, 2)),
            ("Score Std Deviation", round(float(np.std(df['Total_Score'])), 2)),
            ("Passing Students", int(np.sum(df['Grade'] != 'F'))),
            ("Failing Students", int(np.sum(df['Grade'] == 'F'))),
            ("Pass Rate", str(round(float(np.sum(df['Grade'] != 'F')) / len(df) * 100, 2)) + "%"),
            ("Average Study Hours/Week", round(float(np.mean(df['Study_Hours_per_Week'])), 2)),
            ("Average Stress Level", round(float(np.mean(df['Stress_Level (1-10)'])), 2)),
            ("Average Sleep Hours", round(float(np.mean(df['Sleep_Hours_per_Night'])), 2)),
        ]

        for label, value in analytics_data:
            row = tk.Frame(scroll_frame, bg="#313244")
            row.pack(fill="x", pady=3)

            tk.Label(
                row,
                text=label,
                font=("Arial", 11),
                bg="#313244",
                fg="#6c7086",
                width=25,
                anchor="w"
            ).pack(side="left", padx=15, pady=10)

            tk.Label(
                row,
                text=str(value),
                font=("Arial", 11, "bold"),
                bg="#313244",
                fg="#89b4fa",
                anchor="w"
            ).pack(side="left", padx=15)

    def assign_grade(self):
        self.clear_main()

        tk.Label(
            self.main_frame,
            text="Assign Grade",
            font=("Arial", 22, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=30, pady=(30, 20))

        fields = [
            ("Student ID", "student_id"),
            ("Subject", "subject"),
            ("Grade", "grade"),
        ]

        self.grade_entries = {}

        for label, key in fields:
            tk.Label(
                self.main_frame,
                text=label,
                font=("Arial", 12),
                bg="#1e1e2e",
                fg="#cdd6f4"
            ).pack(anchor="w", padx=30, pady=(10, 3))

            entry = tk.Entry(
                self.main_frame,
                font=("Arial", 12),
                bg="#313244",
                fg="#cdd6f4",
                insertbackground="#cdd6f4",
                relief="flat",
                width=30
            )
            entry.pack(anchor="w", padx=30, ipady=6)
            self.grade_entries[key] = entry

        self.grade_msg = tk.Label(
            self.main_frame,
            text="",
            font=("Arial", 11),
            bg="#1e1e2e",
            fg="#a6e3a1"
        )
        self.grade_msg.pack(anchor="w", padx=30, pady=10)

        tk.Button(
            self.main_frame,
            text="Assign Grade",
            font=("Arial", 12, "bold"),
            bg="#89b4fa",
            fg="#1e1e2e",
            relief="flat",
            cursor="hand2",
            command=self.do_assign_grade
        ).pack(anchor="w", padx=30, ipady=8, ipadx=15)

    def do_assign_grade(self):
        student_id = self.grade_entries["student_id"].get().strip()
        subject = self.grade_entries["subject"].get().strip()
        grade = self.grade_entries["grade"].get().strip()

        if student_id in self.admin.students:
            self.admin.students[student_id].grades[subject] = grade
            self.grade_msg.config(text=f"Grade {grade} assigned to {student_id} for {subject}!", fg="#a6e3a1")
        else:
            self.grade_msg.config(text="Student not found!", fg="#f38ba8")

    def mark_attendance(self):
        self.clear_main()

        tk.Label(
            self.main_frame,
            text="Mark Attendance",
            font=("Arial", 22, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=30, pady=(30, 20))

        fields = [
            ("Student ID", "student_id"),
            ("Attendance Percentage", "attendance"),
        ]

        self.attendance_entries = {}

        for label, key in fields:
            tk.Label(
                self.main_frame,
                text=label,
                font=("Arial", 12),
                bg="#1e1e2e",
                fg="#cdd6f4"
            ).pack(anchor="w", padx=30, pady=(10, 3))

            entry = tk.Entry(
                self.main_frame,
                font=("Arial", 12),
                bg="#313244",
                fg="#cdd6f4",
                insertbackground="#cdd6f4",
                relief="flat",
                width=30
            )
            entry.pack(anchor="w", padx=30, ipady=6)
            self.attendance_entries[key] = entry

        self.attendance_msg = tk.Label(
            self.main_frame,
            text="",
            font=("Arial", 11),
            bg="#1e1e2e",
            fg="#a6e3a1"
        )
        self.attendance_msg.pack(anchor="w", padx=30, pady=10)

        tk.Button(
            self.main_frame,
            text="Mark Attendance",
            font=("Arial", 12, "bold"),
            bg="#89b4fa",
            fg="#1e1e2e",
            relief="flat",
            cursor="hand2",
            command=self.do_mark_attendance
        ).pack(anchor="w", padx=30, ipady=8, ipadx=15)

    def do_mark_attendance(self):
        student_id = self.attendance_entries["student_id"].get().strip()
        attendance = self.attendance_entries["attendance"].get().strip()

        if student_id in self.admin.students:
            self.admin.students[student_id].attendance = attendance
            self.attendance_msg.config(text=f"Attendance updated to {attendance}% for {student_id}!", fg="#a6e3a1")
        else:
            self.attendance_msg.config(text="Student not found!", fg="#f38ba8")

    def send_notification(self):
        self.clear_main()

        tk.Label(
            self.main_frame,
            text="Send Notification",
            font=("Arial", 22, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=30, pady=(30, 20))

        tk.Label(
            self.main_frame,
            text="Student ID",
            font=("Arial", 12),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=30, pady=(10, 3))

        self.notif_id_entry = tk.Entry(
            self.main_frame,
            font=("Arial", 12),
            bg="#313244",
            fg="#cdd6f4",
            insertbackground="#cdd6f4",
            relief="flat",
            width=30
        )
        self.notif_id_entry.pack(anchor="w", padx=30, ipady=6)

        tk.Label(
            self.main_frame,
            text="Message",
            font=("Arial", 12),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=30, pady=(10, 3))

        self.notif_msg_entry = tk.Entry(
            self.main_frame,
            font=("Arial", 12),
            bg="#313244",
            fg="#cdd6f4",
            insertbackground="#cdd6f4",
            relief="flat",
            width=30
        )
        self.notif_msg_entry.pack(anchor="w", padx=30, ipady=6)

        self.notif_status = tk.Label(
            self.main_frame,
            text="",
            font=("Arial", 11),
            bg="#1e1e2e",
            fg="#a6e3a1"
        )
        self.notif_status.pack(anchor="w", padx=30, pady=10)

        tk.Button(
            self.main_frame,
            text="Send Notification",
            font=("Arial", 12, "bold"),
            bg="#89b4fa",
            fg="#1e1e2e",
            relief="flat",
            cursor="hand2",
            command=self.do_send_notification
        ).pack(anchor="w", padx=30, ipady=8, ipadx=15)

    def do_send_notification(self):
        student_id = self.notif_id_entry.get().strip()
        message = self.notif_msg_entry.get().strip()

        if student_id in self.admin.students:
            self.admin.students[student_id].notifications.append(message)
            self.notif_status.config(text=f"Notification sent to {student_id}!", fg="#a6e3a1")
        else:
            self.notif_status.config(text="Student not found!", fg="#f38ba8")

    def student_report(self):
        self.clear_main()

        tk.Label(
            self.main_frame,
            text="Student Report",
            font=("Arial", 22, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=30, pady=(30, 20))

        search_frame = tk.Frame(self.main_frame, bg="#1e1e2e")
        search_frame.pack(anchor="w", padx=30, pady=10)

        tk.Label(
            search_frame,
            text="Enter Student ID:",
            font=("Arial", 12),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(side="left", padx=(0, 10))

        self.report_entry = tk.Entry(
            search_frame,
            font=("Arial", 12),
            bg="#313244",
            fg="#cdd6f4",
            insertbackground="#cdd6f4",
            relief="flat",
            width=20
        )
        self.report_entry.pack(side="left", ipady=6)

        tk.Button(
            search_frame,
            text="Generate Report",
            font=("Arial", 11, "bold"),
            bg="#89b4fa",
            fg="#1e1e2e",
            relief="flat",
            cursor="hand2",
            command=self.do_student_report
        ).pack(side="left", padx=10, ipady=6, ipadx=10)

        self.report_frame = tk.Frame(self.main_frame, bg="#1e1e2e")
        self.report_frame.pack(fill="both", expand=True, padx=30, pady=20)

    def do_student_report(self):
        for widget in self.report_frame.winfo_children():
            widget.destroy()

        student_id = self.report_entry.get().strip()

        if student_id in self.admin.students:
            student = self.admin.students[student_id]

            details = [
                ("Student ID", student.student_id),
                ("Full Name", f"{student.first_name} {student.last_name}"),
                ("Email", student.email),
                ("Phone", student.phone),
                ("Age", student.age),
                ("Gender", student.gender),
                ("Department", student.department),
                ("Grade", student.grade),
                ("Midterm Score", student.midterm_score),
                ("Final Score", student.final_score),
                ("Assignments Avg", student.assignments_avg),
                ("Quizzes Avg", student.quizzes_avg),
                ("Participation Score", student.participation_score),
                ("Projects Score", student.projects_score),
                ("Total Score", student.total_score),
                ("Attendance", f"{student.attendance}%"),
                ("Study Hours/Week", student.study_hours_per_week),
                ("Stress Level", student.stress_level),
                ("Sleep Hours/Night", student.sleep_hours_per_night),
            ]

            for label, value in details:
                row = tk.Frame(self.report_frame, bg="#313244")
                row.pack(fill="x", pady=2)

                tk.Label(
                    row,
                    text=label,
                    font=("Arial", 10),
                    bg="#313244",
                    fg="#6c7086",
                    width=20,
                    anchor="w"
                ).pack(side="left", padx=15, pady=8)

                tk.Label(
                    row,
                    text=str(value),
                    font=("Arial", 10),
                    bg="#313244",
                    fg="#cdd6f4",
                    anchor="w"
                ).pack(side="left", padx=15)
        else:
            tk.Label(
                self.report_frame,
                text="Student not found!",
                font=("Arial", 12),
                bg="#1e1e2e",
                fg="#f38ba8"
            ).pack(pady=20)

    def logout(self):
        confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if confirm:
            self.root.destroy()