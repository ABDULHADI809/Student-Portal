import tkinter as tk
from tkinter import messagebox

class LoginScreen:
    def __init__(self, root, admin):
        self.root = root
        self.admin = admin
        self.root.title("Student Portal - Login")
        self.root.geometry("500x600")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)

        self.selected_role = tk.StringVar(value="Student")

        self.build_ui()

    def build_ui(self):
        tk.Label(
            self.root,
            text="Student Portal",
            font=("Arial", 28, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(pady=(50, 5))

        tk.Label(
            self.root,
            text="Welcome Back!",
            font=("Arial", 14),
            bg="#1e1e2e",
            fg="#6c7086"
        ).pack(pady=(0, 30))

        tk.Label(
            self.root,
            text="Login As",
            font=("Arial", 12),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack()

        role_frame = tk.Frame(self.root, bg="#1e1e2e")
        role_frame.pack(pady=10)

        tk.Radiobutton(
            role_frame,
            text="Student",
            variable=self.selected_role,
            value="Student",
            font=("Arial", 12),
            bg="#1e1e2e",
            fg="#cdd6f4",
            selectcolor="#313244",
            activebackground="#1e1e2e",
            activeforeground="#cdd6f4"
        ).pack(side="left", padx=20)

        tk.Radiobutton(
            role_frame,
            text="Admin",
            variable=self.selected_role,
            value="Admin",
            font=("Arial", 12),
            bg="#1e1e2e",
            fg="#cdd6f4",
            selectcolor="#313244",
            activebackground="#1e1e2e",
            activeforeground="#cdd6f4"
        ).pack(side="left", padx=20)

        tk.Label(
            self.root,
            text="Email",
            font=("Arial", 12),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=80, pady=(20, 5))

        self.email_entry = tk.Entry(
            self.root,
            font=("Arial", 12),
            bg="#313244",
            fg="#cdd6f4",
            insertbackground="#cdd6f4",
            relief="flat",
            width=30
        )
        self.email_entry.pack(ipady=8, padx=80)

        tk.Label(
            self.root,
            text="Password",
            font=("Arial", 12),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(anchor="w", padx=80, pady=(15, 5))

        self.password_entry = tk.Entry(
            self.root,
            font=("Arial", 12),
            bg="#313244",
            fg="#cdd6f4",
            insertbackground="#cdd6f4",
            relief="flat",
            width=30,
            show="*"
        )
        self.password_entry.pack(ipady=8, padx=80)

        tk.Button(
            self.root,
            text="Login",
            font=("Arial", 13, "bold"),
            bg="#89b4fa",
            fg="#1e1e2e",
            relief="flat",
            width=20,
            cursor="hand2",
            command=self.handle_login
        ).pack(pady=30, ipady=8)

        self.error_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 11),
            bg="#1e1e2e",
            fg="#f38ba8"
        )
        self.error_label.pack()

    def handle_login(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        role = self.selected_role.get()

        if not email or not password:
            self.error_label.config(text="Please fill in all fields!")
            return

        if role == "Admin":
            if email == "admin@portal.com" and password == "admin123":
                self.error_label.config(text="")
                self.root.destroy()
                from view.admin_dashboard import AdminDashboard
                new_root = tk.Tk()
                AdminDashboard(new_root, self.admin)
                new_root.mainloop()
            else:
                self.error_label.config(text="Invalid admin credentials!")

        elif role == "Student":
            found = False
            for student in self.admin.students.values():
                if student.email == email:
                    result = student.login(password)
                    if result == "Login Successful":
                        self.error_label.config(text="")
                        self.root.destroy()
                        from view.student_dashboard import StudentDashboard
                        new_root = tk.Tk()
                        StudentDashboard(new_root, student)
                        new_root.mainloop()
                        found = True
                        break
                    else:
                        self.error_label.config(text="Incorrect password!")
                        found = True
                        break
            if not found:
                self.error_label.config(text="Student not found!")