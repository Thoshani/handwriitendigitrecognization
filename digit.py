import tkinter as tk
from PIL import Image, ImageDraw, ImageOps
import numpy as np
import tensorflow as tf
import os

# Disable OneDNN warning
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Load trained model
model = tf.keras.models.load_model("digit_model.h5")

# Create GUI window
window = tk.Tk()
window.title("Digit Recognizer")
window.geometry("400x500")
window.configure(bg="#f0f4f7")

canvas_width, canvas_height = 280, 280

# Create canvas frame
canvas_frame = tk.Frame(window, bg="#f0f4f7")
canvas_frame.pack(pady=20)

canvas = tk.Canvas(canvas_frame, width=canvas_width, height=canvas_height, bg='white', bd=2, relief="ridge")
canvas.pack()

# PIL image for drawing
image1 = Image.new("L", (canvas_width, canvas_height), 'white')
draw = ImageDraw.Draw(image1)

# Draw lines with mouse
def draw_lines(event):
    x, y = event.x, event.y
    r = 4
    canvas.create_oval(x - r, y - r, x + r, y + r, fill='black')
    draw.ellipse([x - r, y - r, x + r, y + r], fill='black')

canvas.bind("<B1-Motion>", draw_lines)

# Predict digit from canvas
def predict_digit():
    img = image1.resize((28, 28))
    img = ImageOps.invert(img)

    img_array = np.array(img)

    # Find bounding box and crop
    bbox = Image.fromarray(img_array).getbbox()
    if bbox:
        img_array = Image.fromarray(img_array).crop(bbox).resize((20, 20), Image.LANCZOS)

    # Paste into 28x28 image
    new_img = Image.new('L', (28, 28), 0)
    new_img.paste(img_array, (4, 4))

    # Normalize and reshape
    img_array = np.array(new_img).astype('float32') / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    # Predict
    prediction = model.predict(img_array)
    digit = np.argmax(prediction)

    result_label.config(text=f" Predicted Digit: {digit}")

# Clear canvas
def clear_canvas():
    canvas.delete("all")
    draw.rectangle([0, 0, canvas_width, canvas_height], fill='white')
    result_label.config(text="")

# Buttons
def styled_button(text, command):
    return tk.Button(window, text=text, command=command, font=("Helvetica", 12, "bold"),
                     bg="#4CAF50", fg="white", padx=10, pady=5, bd=0, relief="raised")

styled_button(" Predict", predict_digit).pack(pady=5)
styled_button(" Clear", clear_canvas).pack(pady=5)

# Label for result
result_label = tk.Label(window, text="", font=("Helvetica", 20), bg="#f0f4f7", fg="#333")
result_label.pack(pady=20)

# Run the app
window.mainloop()
