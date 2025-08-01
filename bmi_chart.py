# bmi_chart.py

import matplotlib.pyplot as plt

def draw_bmi_chart(history):
    dates = [row[0] for row in history]
    bmis = [float(row[1]) for row in history]

    plt.figure(figsize=(6, 4))
    plt.plot(dates, bmis, marker='o', color='blue')
    plt.title("BMI 歷史記錄")
    plt.xlabel("日期")
    plt.ylabel("BMI")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
