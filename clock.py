import tkinter as tk
import time

def update_clock():
    current_time = time.strftime("\n\nTime : %I:%M:%S %p\n %A\n %B %d, %Y\n\n\n\t\t ID:C221050")
    # current_time = time.strftime("\n\n\tRayhan")
    clock_label.config(text=current_time)
    clock_label.after(2000, update_clock)

root = tk.Tk()
root.title("Digital Clock by The mRu ")

clock_label = tk.Label(root, font=("times", 40, "italic bold"), bg="gray")
clock_label.pack(fill="both", expand=True)

update_clock()
root.mainloop()
