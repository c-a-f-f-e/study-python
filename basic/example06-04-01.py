# coding:utf-8
import tkinter as tk

root = tk.Tk()
root.geometry("400x150")
root.title("数当てゲーム")

labell = tk.Label(root, text="数を入力してね", font=("Helvetica", 14))
labell.place(x = 20, y = 20)

editbox1 = tk.Entry(width = 4, font=("Helvetica", 28))
editbox1.place(x = 120, y = 60)

button1 = tk.Button(root, text = "チェック", font=("Helvetica", 14))
button1.place(x = 220, y = 60)

root.mainloop()