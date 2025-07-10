import random
import time

class SortVisualizer:
    def __init__(self, canvas):
        self.canvas = canvas
        self.array = [random.randint(10, 400) for _ in range(30)]
        self.paused = False
        self.delay = 0.1

    def reset_array(self):
        self.array = [random.randint(10, 400) for _ in range(30)]

    def set_delay(self, speed_label):
        speeds = {"Slow": 0.2, "Medium": 0.1, "Fast": 0.03}
        self.delay = speeds.get(speed_label, 0.1)

    def toggle_pause(self):
        self.paused = not self.paused

    def wait_or_pause(self):
        while self.paused:
            self.canvas.update()
            time.sleep(0.05)

    def draw_array(self, highlight_indices=[]):
        self.canvas.delete("all")
        c_width = 800
        c_height = 500
        bar_width = c_width / len(self.array)
        for i, val in enumerate(self.array):
            x0 = i * bar_width
            y0 = c_height - val
            x1 = (i + 1) * bar_width
            y1 = c_height
            color = "red" if i in highlight_indices else "blue"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        self.canvas.update()

    def visualize_bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(n - i - 1):
                self.wait_or_pause()
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                self.draw_array(highlight_indices=[j, j+1])
                time.sleep(self.delay)
