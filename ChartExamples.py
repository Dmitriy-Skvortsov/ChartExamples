# Примеры построения графиков

import tkinter as tk

# Функция закрытия программы
def do_close():
    window.destroy()

# Создание главного окна
window = tk.Tk()
window.geometry("450x450")
window.title("Примеры построения графиков")

# Добавление метки заголовка
lblTitle = tk.Label(text = "Примеры построения графиков", font = ('helvetica', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x=55, y=55)


# Добавление кнопки закрытия программы
btnClouse = tk.Button(window, text="Закрыть", font = ('Helvetica', 10, 'bold'), command = do_close)
btnClouse.place(x=330, y=400, width=90, height=30)

# Запуск цикла mainloop
window.mainloop()