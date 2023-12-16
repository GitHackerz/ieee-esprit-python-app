import tkinter as tk
from tkinter import filedialog, messagebox

import pandas as pd
from PIL import Image, ImageTk


def convert_excel_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        try:
            df = pd.read_excel(file_path)
            df['date'] = df['date'].astype(str)
            json_file_path = file_path.rsplit('.', 1)[0] + '.json'
            df.to_json(json_file_path, orient='records')
            messagebox.showinfo("Conversion Successful", f"Excel file converted to {json_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Main Window")
        master.geometry("400x200")  # Adjusted width and height to better accommodate the logo

        # Add logo
        logo_image = Image.open("Logo.png")  # Replace with the actual file path
        logo_image = logo_image.resize((250, 100), Image.LANCZOS)  # Use LANCZOS resampling
        logo_image = ImageTk.PhotoImage(logo_image)

        logo_label = tk.Label(master, image=logo_image)
        logo_label.image = logo_image  # Keep a reference to the image object
        logo_label.pack()

        # Create a Frame for the options
        self.options_frame = tk.Frame(master)
        self.options_frame.pack(pady=20)

        # Convert Button
        convert_button = tk.Button(self.options_frame, text="Convert Excel to JSON", command=convert_excel_file)
        convert_button.pack()


def main():
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
