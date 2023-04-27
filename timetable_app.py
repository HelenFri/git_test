from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime, timedelta


def generator_timetable():
    pattern = '%H:%M'
    try:
        start, end = datetime.strptime(start_tf.get(), pattern), datetime.strptime(end_tf.get(), pattern)
        lesson = timedelta(minutes=int(lesson_tf.get()))
        pause = timedelta(minutes=int(pause_tf.get()))
        data = [('doc', '*.doc')]
        filepath = filedialog.asksaveasfilename(filetypes=data, defaultextension=".txt")
        file = open(filepath, 'w', encoding='utf-8')
        n = 1
        while start <= (end - lesson):
            file.write(f'Урок {n}-й:   ')
            file.write(datetime.strftime(start, pattern))
            file.write(' - ')
            start += lesson
            file.write(datetime.strftime(start, pattern))
            file.write('\n\n')
            start += pause
            n += 1
        file.close()
        messagebox.showinfo('Готово', "Расписание создано")
    except:
        messagebox.showinfo('Ошибка', "Неправильный формат введенных данных!")


window = Tk()
window.title("Генератор расписания занятий по времени")
header = Label(text='Генератор расписания занятий по времени', fg="black", font="21")
header.pack(expand=True)
window.geometry('500x250')

frame = Frame(
   window,
   padx=10,
   pady=10
)
frame.pack(expand=True)

start_lb = Label(
    frame,
    text="Введите начало смены в виде ЧЧ:ММ "
)
start_lb.grid(row=3, column=1, sticky="w")

end_lb = Label(
    frame,
    text="Введите окончание смены в виде ЧЧ:ММ ",
)
end_lb.grid(row=4, column=1, sticky="w")

lesson_lb = Label(
    frame,
    text="Введите продолжительность урока в минутах "
)
lesson_lb.grid(row=5, column=1, sticky="w")

pause_lb = Label(
    frame,
    text="Введите продолжительность перемены в минутах ",
)
pause_lb.grid(row=6, column=1, sticky="w")

start_tf = Entry(
    frame,
)
start_tf.grid(row=3, column=2, pady=5)

end_tf = Entry(
    frame,
)
end_tf.grid(row=4, column=2, pady=5)

lesson_tf = Entry(
    frame,
)
lesson_tf.grid(row=5, column=2, pady=5)

pause_tf = Entry(
    frame,
)
pause_tf.grid(row=6, column=2, pady=5)


gen_btn = Button(
    frame,
    text='Создать расписание',
    command=generator_timetable
)
gen_btn.grid(row=7, column=2)

window.mainloop()
