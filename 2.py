from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk

def round_formula(x, y, r):
    img = Image.new('RGB', (500, 500), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    for i in range(-r*10, r*10+1):
        for j in range(-r*10, r*10+1):
            if abs(i**2/100 + j**2/100 - r**2) <= 1:
                draw.point((x + i//10, y + j//10), fill=(0, 255, 0))
    return np.array(img)

def trigon(x, y, r):
    img = Image.new('RGB', (500, 500), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    for i in range(360):
        angle = i * np.pi / 180
        px = x + r * np.cos(angle)
        py = y + r * np.sin(angle)
        draw.point((int(px), int(py)), fill=(0, 255, 0))
    return np.array(img)

def bresenham(x, y, r):
    img = Image.new('RGB', (500, 500), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    d = 3 - 2 * r
    px, py = 0, r
    while px <= py:
        draw.point((x + px, y + py), fill=(0, 255, 0))
        draw.point((x + py, y + px), fill=(0, 255, 0))
        draw.point((x - px, y + py), fill=(0, 255, 0))
        draw.point((x - py, y + px), fill=(0, 255, 0))
        draw.point((x + px, y - py), fill=(0, 255, 0))
        draw.point((x + py, y - px), fill=(0, 255, 0))
        draw.point((x - px, y - py), fill=(0, 255, 0))
        draw.point((x - py, y - px), fill=(0, 255, 0))
        if d < 0:
            d += 4 * px + 6
        else:
            d += 4 * (px - py) + 10
            py -= 1
        px += 1
    return np.array(img)

class AlgorithmPlot(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Алгоритмы")
        self.geometry("500x500")
        
        self.label_center = tk.Label(self, text="Координаты центра окружности (x, y):")
        self.label_center.pack(pady=5)
        
        self.entry_x = tk.Entry(self)
        self.entry_x.pack(pady=5)
        self.entry_y = tk.Entry(self)
        self.entry_y.pack(pady=5)

        self.label_radius = tk.Label(self, text="Радиус окружности:")
        self.label_radius.pack(pady=5)
        
        self.entry_r = tk.Entry(self)
        self.entry_r.pack(pady=5)
        
        self.label_algorithm = tk.Label(self, text="Выберите алгоритм:")
        self.label_algorithm.pack(pady=5)
        
        self.algorithm_combobox = ttk.Combobox(self, values=["Тригонометрический алгоритм", "Алгоритм Брезенхема", "Формула круга"])
        self.algorithm_combobox.pack(pady=5)
        self.algorithm_combobox.current(0)

        self.button_plot = tk.Button(self, text="Построить", command=self.plot)
        self.button_plot.pack(pady=20)

    def plot(self):
        x = int(self.entry_x.get())
        y = int(self.entry_y.get())
        r = int(self.entry_r.get())
        algorithm = self.algorithm_combobox.get()

        if algorithm == "Тригонометрический алгоритм":
            img = trigon(x, y, r)
        elif algorithm == "Алгоритм Брезенхема":
            img = bresenham(x, y, r)
        elif algorithm == "Формула круга":
            img = round_formula(x, y, r)
        
        plt.imshow(img)
        plt.title(algorithm)
        plt.axis('off')
        plt.show()

def main():
    app = AlgorithmPlot()
    app.mainloop()

if __name__ == "__main__":
    main()
