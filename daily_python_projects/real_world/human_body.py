import tkinter as tk
from PIL import Image, ImageTk
import cairosvg

class AnatomicalViewer:
    def __init__(self, root, svg_path):
        self.root = root
        self.root.title("Human Anatomy Viewer with Diabetic Impact")

        # Convert SVG to PNG for display
        cairosvg.svg2png(url=svg_path, write_to="temp.png")

        # Load PNG
        self.image = Image.open("temp.png")
        self.tk_image = ImageTk.PhotoImage(self.image)

        # Create canvas
        self.canvas = tk.Canvas(root, width=self.image.width, height=self.image.height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Display image
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)

        # Bind mouse scroll for zoom
        self.canvas.bind("<MouseWheel>", self.zoom)

    def zoom(self, event):
        factor = 1.1 if event.delta > 0 else 0.9
        new_width = int(self.image.width * factor)
        new_height = int(self.image.height * factor)

        # Resize image
        resized_image = self.image.resize((new_width, new_height), Image.ANTIALIAS)
        self.tk_image = ImageTk.PhotoImage(resized_image)

        # Update canvas
        self.canvas.config(width=new_width, height=new_height)
        self.canvas.itemconfig(self.image_on_canvas, image=self.tk_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = AnatomicalViewer(root, "anatomy.svg")  # Replace with your anatomical SVG path
    root.mainloop()
