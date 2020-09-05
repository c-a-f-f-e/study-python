# coding;utf-8
import tkinter as tk

# ウィンドウを開く
root = tk.Tk()
root.geometry("600x400")

# Canvasを開く
canvas = tk.Canvas(root, width =600, height =400, bg="white")
canvas.place(x = 0)