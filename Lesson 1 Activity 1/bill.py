import tkinter as tk

root = tk.Tk()
root.title("Number Pad")
root.geometry('250x300')

# Use grid only — no pack
nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ["#", 0, "*"]]

# Configure rows and columns
for i in range(4):
    root.rowconfigure(i, weight=1, minsize=50)
for j in range(3):
    root.columnconfigure(j, weight=1, minsize=75)

# Create number pad buttons
for i in range(4):
    for j in range(3):
        frame = tk.Frame(root, relief=tk.SUNKEN, borderwidth=1, bg="#d0efff")
        frame.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

        label = tk.Label(frame, text=nums[i][j], bg="#d0efff", font=("Arial", 16))
        label.pack(expand=True, fill="both")

root.mainloop()
