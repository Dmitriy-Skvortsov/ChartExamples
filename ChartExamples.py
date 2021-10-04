# Примеры построения графиков

import tkinter as tk
# Импорт внешних файлов
import chart1
import chart2
import chart3

# Функция закрытия программы
def do_close():
    window.destroy()

# Создание главного окна
window = tk.Tk()
window.geometry("450x550")
window.title("Примеры построения графиков")

# Добавление метки заголовка
lblTitle = tk.Label(text = "Примеры построения графиков", font = ('helvetica', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x=55, y=55)

# Добавление кнопки и метки для графика 1
btnChart1 = tk.Button(window, text="График 1", font = ('Helvetica', 10, 'bold'), command=chart1.plot_chart)
btnChart1.place(x=40, y=115, width=90, height=30)

lblChart1 = tk.Label(text = "График синуса matplotlib")
lblChart1.place(x=170, y=122)

# Добавление кнопки и метки для графика 2
btnChart1 = tk.Button(window, text="График 2", font = ('Helvetica', 10, 'bold'), command=chart2.plot_chart)
btnChart1.place(x=40, y=165, width=90, height=30)

lblChart1 = tk.Label(text = "Нормальное распределение")
lblChart1.place(x=170, y=172)

# Добавление кнопки и метки для графика 3
btnChart1 = tk.Button(window, text="График 3", font = ('Helvetica', 10, 'bold'), command=chart3.plot_chart)
btnChart1.place(x=40, y=215, width=90, height=30)

lblChart1 = tk.Label(text = "Гистограмма")
lblChart1.place(x=170, y=222)

# Добавление кнопки и метки для графика 4
btnChart1 = tk.Button(window, text="График 4", font = ('Helvetica', 10, 'bold'), command=chart2.plot_chart2)
btnChart1.place(x=40, y=265, width=90, height=30)

lblChart1 = tk.Label(text = "Нормальное распределение 3 графика")
lblChart1.place(x=170, y=272)

# Добавление кнопки и метки для графика 5
btnChart1 = tk.Button(window, text="График 5", font = ('Helvetica', 10, 'bold'), command=chart3.plot_chart)
btnChart1.place(x=40, y=315, width=90, height=30)

lblChart1 = tk.Label(text = "Гистограмма")
lblChart1.place(x=170, y=322)

# Добавление кнопки и метки для графика 6
btnChart1 = tk.Button(window, text="График 6", font = ('Helvetica', 10, 'bold'), command=chart3.plot_chart)
btnChart1.place(x=40, y=365, width=90, height=30)

lblChart1 = tk.Label(text = "Гистограмма")
lblChart1.place(x=170, y=372)

# Добавление кнопки и метки для графика 7
btnChart1 = tk.Button(window, text="График 7", font = ('Helvetica', 10, 'bold'), command=chart3.plot_chart)
btnChart1.place(x=40, y=415, width=90, height=30)

lblChart1 = tk.Label(text = "Гистограмма")
lblChart1.place(x=170, y=422)

# Добавление кнопки закрытия программы
btnClouse = tk.Button(window, text="Закрыть", font = ('Helvetica', 10, 'bold'), command = do_close)
btnClouse.place(x=330, y=500, width=90, height=30)

# Запуск цикла mainloop
window.mainloop()
