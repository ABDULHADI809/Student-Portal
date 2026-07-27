import tkinter as tk
from data_loader import setup_portal
from view.login import LoginScreen

# Load everything from dataset
admin = setup_portal("data/Students_Performance_Dataset_Updated.csv")

# Launch login screen
root = tk.Tk()
app = LoginScreen(root, admin)
root.mainloop()
