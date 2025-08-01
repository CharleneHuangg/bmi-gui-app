# bmi_gui.py

import tkinter as tk
from tkinter import messagebox
import datetime
import csv
from bmi_calc import calculate_bmi
from bmi_chart import draw_bmi_chart

def start_gui():
    bmi_history = []

    def on_calculate():
        try:
            weight = float(weight_entry.get())
            height = float(height_entry.get())
            bmi = calculate_bmi(weight, height)

            today = datetime.date.today().isoformat()
            bmi_history.append((today, bmi))

            messagebox.showinfo("BMI 結果", f"你的 BMI 是 {bmi}")

            # 存入檔案
            with open("bmi_data.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([today, bmi])

        except ValueError:
            messagebox.showerror("錯誤", "請輸入有效的數字")

    def on_show_chart():
        draw_bmi_chart(bmi_history)

    window = tk.Tk()
    window.title("BMI 計算器")

    tk.Label(window, text="體重（kg）").grid(row=0, column=0)
    weight_entry = tk.Entry(window)
    weight_entry.grid(row=0, column=1)

    tk.Label(window, text="身高（cm）").grid(row=1, column=0)
    height_entry = tk.Entry(window)
    height_entry.grid(row=1, column=1)

    tk.Button(window, text="計算", command=on_calculate).grid(row=2, column=0)
    tk.Button(window, text="顯示圖表", command=on_show_chart).grid(row=2, column=1)

    window.mainloop()
