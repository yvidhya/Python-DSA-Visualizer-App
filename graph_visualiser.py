import time
from collections import deque

class GraphVisualizer:
    def __init__(self, canvas):
        self.canvas = canvas
        self.paused = False
        self.delay = 0.5

        self.nodes = {
            0: (100, 100),
            1: (300, 100),
            2: (500, 100),
            3: (200, 250),
            4: (400, 250)
        }

        self.edges = {
            0: [1, 3],
            1: [0, 2],
            2: [1, 4],
            3: [0, 4],
            4: [2, 3]
        }

    def set_delay(self, speed_label):
        speeds = {"Slow": 1.0, "Medium": 0.5, "Fast": 0.2}
        self.delay = speeds.get(speed_label, 0.5)

    def toggle_pause(self):
        self.paused = not self.paused

    def wait_or_pause(self):
        while self.paused:
            self.canvas.update()
            time.sleep(0.05)

    def draw_graph(self, visited=set()):
        self.canvas.delete("all")
        for src in self.edges:
            for dest in self.edges[src]:
                x1, y1 = self.nodes[src]
                x2, y2 = self.nodes[dest]
                self.canvas.create_line(x1, y1, x2, y2)
        for node, (x, y) in self.nodes.items():
            color = "green" if node in visited else "gray"
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=color)
            self.canvas.create_text(x, y, text=str(node), fill="white")
        self.canvas.update()

    def visualize_bfs(self):
        start_node = 0
        visited = set()
        queue = deque([start_node])

        while queue:
            self.wait_or_pause()
            current = queue.popleft()
            if current not in visited:
                visited.add(current)
                self.draw_graph(visited)
                time.sleep(self.delay)
                for neighbor in self.edges[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)
