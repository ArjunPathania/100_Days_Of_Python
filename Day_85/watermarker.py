from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image, ImageDraw, ImageFont
import os


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarking Desktop App")
        self.root.minsize(width=800, height=600)
        self.root.resizable(width=True, height=True)

        self.frame = Frame(self.root)
        self.frame.pack(expand=True)

        Label(self.frame, text="Welcome to the Image Watermarking App",
              font=("Helvetica", 20, "bold")).grid(row=0, column=0, columnspan=3, pady=(20, 10))

        Label(self.frame, text="Use this app to watermark an image",
              font=("Helvetica", 12)).grid(row=1, column=0, columnspan=3, pady=(0, 20))

        Button(self.frame, text='Open Image', width=20,
               command=self.open_img).grid(row=2, column=0, pady=10, padx=10)

        Button(self.frame, text='Mark Image', width=20,
               command=self.add_text_watermark).grid(row=2, column=1, pady=10, padx=10)

        Button(self.frame, text='Close', width=20,
               command=self.root.quit).grid(row=2, column=2, pady=10, padx=10)

        Label(self.frame, text="Enter Watermark", font=("Helvetica", 12)).grid(row=3, column=0, columnspan=3, pady=(10, 0))

        self.watermark_entry = Entry(self.frame, width=40)
        self.watermark_entry.grid(row=4, column=0, columnspan=3)

        self.image_panel = None
        self.img = None
        self.img_path = None

    def open_filename(self):
        return filedialog.askopenfilename(
            title='Open Image File',
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )

    def open_img(self):
        file_path = self.open_filename()
        if not file_path:
            return

        self.img_path = file_path
        img = Image.open(file_path).convert("RGBA")
        img = img.resize((400, 400), Image.LANCZOS)

        self.img = img
        img_tk = ImageTk.PhotoImage(img)

        if self.image_panel is None:
            self.image_panel = Label(self.frame, image=img_tk)
            self.image_panel.image = img_tk
            self.image_panel.grid(row=5, column=0, columnspan=3, pady=20)
        else:
            self.image_panel.configure(image=img_tk)
            self.image_panel.image = img_tk

    def add_text_watermark(self, font_size=30, opacity=128):
        if not self.img:
            messagebox.showerror("Error", "No image loaded.")
            return

        text = self.watermark_entry.get().strip()
        if not text:
            messagebox.showerror("Error", "Please enter a watermark text.")
            return

        base_image = self.img.copy()
        width, height = base_image.size

        transparent_layer = Image.new("RGBA", base_image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(transparent_layer)

        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()

        # Pillow 10+ compatible text size calculation
        try:
            bbox = font.getbbox(text)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
        except AttributeError:
            text_width, text_height = font.getsize(text)

        x = (width - text_width) // 2
        y = (height - text_height) // 2

        draw.text((x, y), text, font=font, fill=(255, 255, 255, opacity))
        watermarked_image = Image.alpha_composite(base_image, transparent_layer).convert("RGB")

        import os
        dir_name = os.path.dirname(self.img_path)
        file_name = os.path.basename(self.img_path)
        name, ext = os.path.splitext(file_name)
        output_path = os.path.join(dir_name, f"{name}_watermarked.jpg")

        watermarked_image.save(output_path)
        messagebox.showinfo("Success", f"Watermarked image saved to:\n{output_path}")



if __name__ == "__main__":
    root = Tk()
    app = WatermarkApp(root)
    root.mainloop()
