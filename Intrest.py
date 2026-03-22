import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        p = float(entry_principal.get())
        t = float(entry_time.get())
        r = float(entry_rate.get())

        # Simple Interest
        si = (p * t * r) / 100

        # Compound Interest (annually compounded)
        ci = p * ((1 + r / 100) ** t) - p

        result_si.config(text=f"Simple Interest: {si:.2f}")
        result_ci.config(text=f"Compound Interest: {ci:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create window
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x300")

# Labels and Entries
tk.Label(root, text="Principal Amount").pack(pady=5)
entry_principal = tk.Entry(root)
entry_principal.pack()

tk.Label(root, text="Time (years)").pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack()

tk.Label(root, text="Rate of Interest (%)").pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack()

# Calculate Button
tk.Button(root, text="Calculate", command=calculate_interest).pack(pady=10)

# Result Labels
result_si = tk.Label(root, text="Simple Interest: ")
result_si.pack(pady=5)

result_ci = tk.Label(root, text="Compound Interest: ")
result_ci.pack(pady=5)

# Run application
root.mainloop()