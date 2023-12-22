import tkinter as tk

class PointSelectionApp:
    def __init__(self, root, x_label='X-Axis', y_label='Y-Axis'):
        self.scalingFactor = 1
        self.width = 1000
        self.height = 1000
        self.root = root
        self.root.title("Point Selection GUI")

        # Set up the canvas
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg='white')
        self.canvas.pack()

        # Add axis labels
        self.canvas.create_text(self.width / 2, self.height - 10, text=x_label)
        self.canvas.create_text(10, self.height / 2, text=y_label, angle=90)

        # Bind the canvas to mouse events
        self.canvas.bind("<Button-1>", self.add_point)
        self.canvas.bind("<Motion>", self.update_lines)

        # List to store points
        self.points = []

        # Initialize lines for cursor follow
        self.v_line = self.canvas.create_line(0, 0, 0, self.height, dash=(4, 2))
        self.h_line = self.canvas.create_line(0, 0, self.width, 0, dash=(4, 2))

        # Frame to hold the points list and the buttons
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Scrollbar for the points list
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Listbox to display points
        self.listbox = tk.Listbox(self.frame, yscrollcommand=self.scrollbar.set)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        # Configure scrollbar
        self.scrollbar.config(command=self.listbox.yview)

        # Button to clear points
        self.clear_button = tk.Button(root, text="Clear Points", command=self.clear_points)
        self.clear_button.pack(side=tk.LEFT)

        # Button to finalize the points selection
        self.done_button = tk.Button(root, text="Done", command=self.finalize_points)
        self.done_button.pack(side=tk.RIGHT)

    def getScalingFactor(self):
        return self.scalingFactor
    def setScalingFactor(self, factor):
        self.scalingFactor = factor

    def add_point(self, event):
        # Get mouse click coordinates and flip the y-coordinate
        x, y = event.x, event.y

        # Scale the points back to original resolution and append
        scaled_x, scaled_y = x * self.scalingFactor, (self.height - y) * self.scalingFactor
        self.points.append((scaled_x, scaled_y))

        # Draw a small circle at the click position
        r = 3
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill='black')

        # Add point coordinates to the listbox
        point_number = len(self.points)
        self.listbox.insert(tk.END, f"{point_number}: ({scaled_x}, {scaled_y})")

        # Draw the point number next to the circle
        self.canvas.create_text(x + 10, y, text=str(point_number))

    def update_lines(self, event):
        # Adjust the event's x and y to the scaling factor
        x = (event.x) / self.scalingFactor
        y = (event.y) / self.scalingFactor
        
        # Update vertical line to follow cursor on x-axis
        self.canvas.coords(self.v_line, x * self.scalingFactor, 0, x * self.scalingFactor, self.height)

        # Update horizontal line to follow cursor on flipped y-axis
        self.canvas.coords(self.h_line, 0, y * self.scalingFactor, self.width, y * self.scalingFactor)

        # Update the window title with the current coordinates (flipped y-coordinate)
        self.root.title(f"Point Selection GUI - Cursor: ({x * self.scalingFactor}, {self.height - y * self.scalingFactor})")

    def clear_points(self):
        # Clear the canvas and remove lines
        self.canvas.delete("all")

        # Redraw the cursor follow lines
        self.v_line = self.canvas.create_line(0, 0, 0, self.height, dash=(4, 2))
        self.h_line = self.canvas.create_line(0, 0, self.width, 0, dash=(4, 2))

        # Clear the points list and the listbox
        self.points.clear()
        self.listbox.delete(0, tk.END)

    def finalize_points(self):
        # If there's any action to be taken when points selection is done, it goes here.
        # Remember that the y-coordinates are already flipped.
        self.root.destroy()

    def getPoints(self):
        # If you need to return the points to something expecting traditional tkinter y-coordinates,
        # you would need to flip the y-coordinates back here.
        return self.points

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    app = PointSelectionApp(root)
    root.mainloop()
