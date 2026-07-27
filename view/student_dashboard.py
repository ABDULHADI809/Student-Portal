import tkinter as tk
from tkinter import messagebox

class StudentDashboard:
    def __init__(self, root, student):
        self.root = root
        self.student = student
        self.root.title(f"Student Portal - {student.first_name} {student.last_name}")
        self.root.geometry("1000x650")
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
            text=f"{self.student.first_name}",
            font=("Arial", 16, "bold"),
            bg="#181825",
            fg="#cdd6f4"
        ).pack(pady=(30, 5))

        tk.Label(
            sidebar,
            text=f"{self.student.student_id}",
            font=("Arial", 10),
            bg="#181825",
            fg="#6c7086"
        ).pack(pady=(0, 30))

        sections = [
            ("🏠  Dashboard", self.show_dashboard),
            ("👤  My Profile", self.show_profile),
            ("📊  My Grades", self.show_grades),
            ("📚  My Courses", self.show_courses),
            ("📅  Attendance", self.show_attendance),
            ("🕐  Timetable", self.show_timetable),
            ("📢  Announcements", self.show_announcements),
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
            text=f"Welcome, {self.student.first_name}! 👋",
            font=("Arial", 22, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=30, pady=(30, 5))

        tk.Label(
            self.main_frame,
            text="Here's your academic summary",
            font=("Arial", 12),
            bg="#1e1e2e",
            fg="#6c7086"
        ).pack(anchor="w", padx=30, pady=(0, 30))

        cards_frame = tk.Frame(self.main_frame, bg="#1e1e2e")
        cards_frame.pack(padx=30, fill="x")

        cards = [
            ("Total Score", f"{self.student.total_score}", "#89b4fa"),
            ("Grade", f"{self.student.grade}", "#a6e3a1"),
            ("Attendance", f"{self.student.attendance}%", "#fab387"),
            ("Department", f"{self.student.department}", "#cba6f7"),
        ]

        for title, value, color in cards:
            card = tk.Frame(cards_frame, bg="#313244", width=150, height=100)
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

        tk.Label(
            self.main_frame,
            text="Recent Grades",
            font=("Arial", 16, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=30, pady=(30, 10))

        for subject, score in self.student.grades.items():
            row = tk.Frame(self.main_frame, bg="#313244")
            row.pack(fill="x", padx=30, pady=3)

            tk.Label(
                row,
                text=subject,
                font=("Arial", 11),
                bg="#313244",
                fg="#cdd6f4",
                width=20,
                anchor="w"
            ).pack(side="left", padx=15, pady=8)

            tk.Label(
                row,
                text=str(score),
                font=("Arial", 11, "bold"),
                bg="#313244",
                fg="#89b4fa"
            ).pack(side="right", padx=15)

    def show_profile(self):
        self.clear_main()

        tk.Label(
            self.main_frame,
            text="My Profile",
            font=("Arial", 22, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=30, pady=(30, 20))

        details = [
            ("Student ID", self.student.student_id),
            ("Full Name", f"{self.student.first_name} {self.student.last_name}"),
            ("Email", self.student.email),
            ("Phone", self.student.phone),
            ("Address", self.student.address),
            ("Age", self.student.age),
            ("Gender", self.student.gender),
            ("Department", self.student.department),
        ]

        for label, value in details:
            row = tk.Frame(self.main_frame, bg="#313244")
            row.pack(fill="x", padx=30, pady=3)

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

    def show_grades(self):
        self.clear_main()

        tk.Label(
            self.main_frame,
            text="My Grades",
            font=("Arial", 22, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=30, pady=(30, 20))

        grades = [
            ("Midterm Score", self.student.midterm_score),
            ("Final Score", self.student.final_score),
            ("Assignments Avg", self.student.assignments_avg),
            ("Quizzes Avg", self.student.quizzes_avg),
            ("Participation Score", self.student.participation_score),
            ("Projects Score", self.student.projects_score),
            ("Total Score", self.student.total_score),
            ("Grade", self.student.grade),
        ]

        for label, value in grades:
            row = tk.Frame(self.main_frame, bg="#313244")
            row.pack(fill="x", padx=30, pady=3)

            tk.Label(
                row,
                text=label,
                font=("Arial", 11),
                bg="#313244",
                fg="#6c7086",
                width=20,
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

    def show_courses(self):
        self.clear_main()

        tk.Label(
            self.main_frame,
            text="My Courses",
            font=("Arial", 22, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=30, pady=(30, 20))

        if not self.student.courses:
            tk.Label(
                self.main_frame,
                text="No courses enrolled yet!",
                font=("Arial", 12),
                bg="#1e1e2e",
                fg="#6c7086"
            ).pack(padx=30, pady=20)
        else:
            for i, course in enumerate(self.student.courses, 1):
                row = tk.Frame(self.main_frame, bg="#313244")
                row.pack(fill="x", padx=30, pady=3)

                tk.Label(
                    row,
                    text=f"{i}.",
                    font=("Arial", 11),
                    bg="#313244",
                    fg="#6c7086",
                    width=3
                ).pack(side="left", padx=10, pady=10)

                tk.Label(
                    row,
                    text=course,
                    font=("Arial", 11),
                    bg="#313244",
                    fg="#cdd6f4"
                ).pack(side="left", padx=10)

    def show_attendance(self):
        self.clear_main()

        tk.Label(
            self.main_frame,
            text="My Attendance",
            font=("Arial", 22, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=30, pady=(30, 20))

        row = tk.Frame(self.main_frame, bg="#313244")
        row.pack(fill="x", padx=30, pady=3)

        tk.Label(
            row,
            text="Overall Attendance",
            font=("Arial", 12),
            bg="#313244",
            fg="#6c7086",
            width=20,
            anchor="w"
        ).pack(side="left", padx=15, pady=15)

        tk.Label(
            row,
            text=f"{self.student.attendance}%",
            font=("Arial", 14, "bold"),
            bg="#313244",
            fg="#a6e3a1"
        ).pack(side="left", padx=15)

    def show_timetable(self):
        self.clear_main()

        tk.Label(
            self.main_frame,
            text="My Timetable",
            font=("Arial", 22, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=30, pady=(30, 20))

        if not self.student.timetable:
            tk.Label(
                self.main_frame,
                text="No timetable available yet!",
                font=("Arial", 12),
                bg="#1e1e2e",
                fg="#6c7086"
            ).pack(padx=30, pady=20)
        else:
            for day, schedule in self.student.timetable.items():
                row = tk.Frame(self.main_frame, bg="#313244")
                row.pack(fill="x", padx=30, pady=3)

                tk.Label(
                    row,
                    text=day,
                    font=("Arial", 11, "bold"),
                    bg="#313244",
                    fg="#cba6f7",
                    width=12,
                    anchor="w"
                ).pack(side="left", padx=15, pady=10)

                tk.Label(
                    row,
                    text=schedule,
                    font=("Arial", 11),
                    bg="#313244",
                    fg="#cdd6f4"
                ).pack(side="left", padx=10)

    def show_announcements(self):
        self.clear_main()

        tk.Label(
            self.main_frame,
            text="Announcements",
            font=("Arial", 22, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=30, pady=(30, 20))

        if not self.student.notifications:
            tk.Label(
                self.main_frame,
                text="No announcements yet!",
                font=("Arial", 12),
                bg="#1e1e2e",
                fg="#6c7086"
            ).pack(padx=30, pady=20)
        else:
            for note in self.student.notifications:
                row = tk.Frame(self.main_frame, bg="#313244")
                row.pack(fill="x", padx=30, pady=3)

                tk.Label(
                    row,
                    text=f"• {note}",
                    font=("Arial", 11),
                    bg="#313244",
                    fg="#cdd6f4"
                ).pack(anchor="w", padx=15, pady=10)

    def logout(self):
        confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if confirm:
            self.root.destroy()