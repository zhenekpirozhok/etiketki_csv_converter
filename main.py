import tkinter as tk
from tkinter import filedialog, messagebox
import os
import csv

root = tk.Tk()
root.title("CSV Merger")
root.geometry("400x200")

def select_file():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select a File", filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")))
    if filename:
        interval_window(filename)

def interval_window(filename):
    interval_window = tk.Toplevel(root)
    interval_window.title("Input interval")

    tk.Label(interval_window, text="Введите интервал (целое число):").pack(pady=10)
    interval_entry = tk.Entry(interval_window)
    interval_entry.pack(pady=10)

    def submit_interval():
        try:
            interval = int(interval_entry.get())
            if interval > 0:
                interval_window.destroy()
                convert_csv(filename, interval)
            else:
                messagebox.showerror("Ошибка", "Интервал должен быть больше нуля")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное целое число")

    submit_button = tk.Button(interval_window, text="OK", command=submit_interval)
    submit_button.pack(pady=10)


def convert_csv(file_path, interval):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
            
        new_csv_path = os.path.splitext(file_path)[0] + "_merged.csv"
        with open(new_csv_path, 'w', newline='') as new_file:
            writer = csv.writer(new_file)

            writer.writerow(["Identifikacinis numeris", "Padeklas",	"alk",	"Index"])
            qr = qrcode.get()
            alk = entry.get()

            for i, row in enumerate(data):
                qrName = qr if (i+1) % interval != 0 else qr+"_gr"
                data = row[0].split("\x1d") if len(row) == 1 else row
                print(row)
                print(data)
                writer.writerow([data[0], data[1], alk, qrName])

        messagebox.showinfo("Успех", f"CSV файл успешно объединен в {new_csv_path}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")


label = tk.Label(root, text="Alk:")
label.pack(padx=6, pady=6)

entry = tk.Entry(root)
entry.pack(padx=6, pady=6)
entry.insert(0, "P007138190")

label2 = tk.Label(root, text="QR код:")
label2.pack(padx=6, pady=6)

qrcode = tk.Entry(root)
qrcode.pack(padx=6, pady=6)
qrcode.insert(0, "M1M1_KITI10")

button = tk.Button(root, text="Browse", command=select_file)
button.pack(padx=6, pady=6)

root.mainloop()