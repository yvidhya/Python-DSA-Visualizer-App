import tkinter as tk
from sort_visualiser import SortVisualizer
from graph_visualiser import GraphVisualizer

class DSAVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DSA Visualizer")
        self.root.geometry("900x600")

        self.menu_frame = tk.Frame(root)
        self.menu_frame.pack(side=tk.TOP, fill=tk.X)

        self.canvas = tk.Canvas(root, bg="white", height=500)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.current_algo = None
        self.last_algorithm = None

        # Buttons
        tk.Button(self.menu_frame, text="Bubble Sort", command=self.run_bubble_sort).pack(side=tk.LEFT, padx=10)
        tk.Button(self.menu_frame, text="BFS", command=self.run_bfs).pack(side=tk.LEFT, padx=10)

        # Visualizer instances
        self.sort_visualizer = SortVisualizer(self.canvas)
        self.graph_visualizer = GraphVisualizer(self.canvas)

        # Pause/Resume
        self.pause_btn = tk.Button(self.menu_frame, text="Pause", command=self.toggle_pause)
        self.pause_btn.pack(side=tk.LEFT, padx=10)

        # Speed selector
        self.speed_var = tk.StringVar(value="Medium")
        speed_menu = tk.OptionMenu(self.menu_frame, self.speed_var, "Slow", "Medium", "Fast", command=self.change_speed)
        speed_menu.pack(side=tk.LEFT, padx=10)

        # Status label
        self.status_label = tk.Label(self.menu_frame, text="Status: Ready", fg="blue")
        self.status_label.pack(side=tk.LEFT, padx=10)

        # Replay button
        self.replay_btn = tk.Button(self.menu_frame, text="Play Again", command=self.replay_last)
        self.replay_btn.pack(side=tk.LEFT, padx=10)
        self.replay_btn.config(state=tk.DISABLED)

    def set_buttons_state(self, state):
        for child in self.menu_frame.winfo_children():
            if isinstance(child, tk.Button):
                if child['text'] in ["Bubble Sort", "BFS", "Play Again"]:
                    child.config(state=state)


    def run_bubble_sort(self):
        if self.current_algo == "bfs":
            self.graph_visualizer.toggle_pause()

        self.current_algo = "sort"
        self.last_algorithm = "sort"
        self.canvas.delete("all")
        self.sort_visualizer.reset_array()
        self.sort_visualizer.paused = False

        self.status_label.config(text="Status: Running Bubble Sort")
        self.set_buttons_state(tk.DISABLED)
        self.replay_btn.config(state=tk.DISABLED)

        self.sort_visualizer.visualize_bubble_sort()

        self.status_label.config(text="Status: Bubble Sort Completed")
        self.replay_btn.config(state=tk.NORMAL)
        self.set_buttons_state(tk.NORMAL)

    def run_bfs(self):
        if self.current_algo == "sort":
            self.sort_visualizer.toggle_pause()

        self.current_algo = "bfs"
        self.last_algorithm = "bfs"
        self.canvas.delete("all")
        self.graph_visualizer.paused = False

        self.status_label.config(text="Status: Running BFS")
        self.set_buttons_state(tk.DISABLED)
        self.replay_btn.config(state=tk.DISABLED)

        self.graph_visualizer.visualize_bfs()

        self.status_label.config(text="Status: BFS Completed")
        self.replay_btn.config(state=tk.NORMAL)
        self.set_buttons_state(tk.NORMAL)

    def toggle_pause(self):
        if self.current_algo == "sort":
            self.sort_visualizer.toggle_pause()
            paused = self.sort_visualizer.paused
        elif self.current_algo == "bfs":
            self.graph_visualizer.toggle_pause()
            paused = self.graph_visualizer.paused
        else:
            paused = False

        self.pause_btn.config(text="Resume" if paused else "Pause")
        status = "Paused" if paused else f"{self.current_algo.upper()} Running"
        self.status_label.config(text=f"Status: {status}")

    def change_speed(self, speed_label):
        self.sort_visualizer.set_delay(speed_label)
        self.graph_visualizer.set_delay(speed_label)

    def replay_last(self):
        self.status_label.config(text="Status: Replaying...")
        if self.last_algorithm == "sort":
            self.run_bubble_sort()
        elif self.last_algorithm == "bfs":
            self.run_bfs()


if __name__ == "__main__":
    root = tk.Tk()
    app = DSAVisualizerApp(root)
    root.mainloop()
