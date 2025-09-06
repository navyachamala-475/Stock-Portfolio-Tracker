import tkinter as tk
from tkinter import messagebox

stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "MSFT": 300}

def calculate():
    result_text.delete("1.0", tk.END)
    total = 0
    for stock, var in entry_vars.items():
        try:
            qty = int(var.get() or 0)
        except ValueError:
            messagebox.showerror("Input error", f"Enter a number for {stock}")
            return
        value = qty * stock_prices[stock]
        total += value
        result_text.insert(tk.END, f"{stock} - {qty} shares → ${value}\n")
    result_text.insert(tk.END, f"\nTotal Portfolio Value: ${total}")

root = tk.Tk()
root.title("Stock Portfolio Tracker")

entry_vars = {}
for stock in stock_prices:
    frame = tk.Frame(root)
    frame.pack(padx=8, pady=2, anchor="w")
    tk.Label(frame, text=f"{stock} quantity:").pack(side="left")
    v = tk.StringVar(value="0")
    tk.Entry(frame, textvariable=v, width=6).pack(side="left")
    entry_vars[stock] = v

tk.Button(root, text="Calculate", command=calculate).pack(pady=6)
result_text = tk.Text(root, height=10, width=40)
result_text.pack(padx=8, pady=4)

root.mainloop()