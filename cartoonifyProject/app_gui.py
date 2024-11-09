import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
from cartoonify import cartoonify_image
import os
from datetime import datetime

# Create main window
root = tk.Tk()
root.title("Cartoonify Image")
root.geometry("800x600")
# Folder where images will be saved
SAVE_FOLDER = "saved_images"

# Create the folder if it doesn't exist
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)
# Global variable to store the current image
current_image = None

# Load Image
def load_image():
    global current_image

    # Open file dialog to choose an image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

    if not file_path:
        return

    # Read the image using OpenCV
    original_image = cv2.imread(file_path)
    current_image = original_image

    # Convert image to RGB for displaying in Tkinter (OpenCV uses BGR)
    original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

    # Convert to Image for displaying in Tkinter
    img = Image.fromarray(original_image_rgb)
    img_tk = ImageTk.PhotoImage(image=img)

    # Display image in the window
    image_label.config(image=img_tk)
    image_label.image = img_tk

# Cartoonify Image
def cartoonify():
    global current_image

    if current_image is None:
        messagebox.showerror("Error", "Please upload an image first.")
        return

    # Apply cartoon effect
    cartoon_img = cartoonify_image(current_image)

    # Convert the cartoon image to RGB for displaying
    cartoon_img_rgb = cv2.cvtColor(cartoon_img, cv2.COLOR_BGR2RGB)

    # Convert to Image for Tkinter
    img = Image.fromarray(cartoon_img_rgb)
    img_tk = ImageTk.PhotoImage(image=img)

    # Display cartoonified image
    image_label.config(image=img_tk)
    image_label.image = img_tk

# Save the cartoonified image
def save_image():
    global current_image
    
    if current_image is None:
        messagebox.showerror("Error", "No image to save.")
        return

#Generate a unique filename based on the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_path = os.path.join(SAVE_FOLDER, f"cartoonified_{timestamp}.png")
    
    #save the cartoonified image
    cartoon_img = cartoonify_image(current_image)
    cv2.imwrite(save_path, current_image)
    # file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg;*.jpeg")])

    # if file_path:
    #     cartoon_img = cartoonify_image(current_image)
    #     cv2.imwrite(file_path, cartoon_img)
    messagebox.showinfo("Success", f"Image saved as {save_path}")

# Create Widgets (Buttons, Label, etc.)
load_button = tk.Button(root, text="Open Image", command=load_image)
load_button.pack(pady=10)

cartoon_button = tk.Button(root, text="Cartoonify", command=cartoonify)
cartoon_button.pack(pady=10)

save_button = tk.Button(root, text="Save Image", command=save_image)
save_button.pack(pady=10)

image_label = tk.Label(root)
image_label.pack(pady=20)

# Run the main loop
root.mainloop()
