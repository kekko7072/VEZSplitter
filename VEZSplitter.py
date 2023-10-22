import PyPDF2
import tkinter as tk
from tkinter import filedialog

A4_HEIGHT = 842*2  # Double size due to 100% zoom in One Note app


def split_pdf(input_pdf):
    pdf = PyPDF2.PdfReader(input_pdf)
    output_pdf = PyPDF2.PdfWriter()

    total_height = pdf.pages[0].mediabox.height
    number_of_pages = int(total_height / A4_HEIGHT) + 1

    for i in range(number_of_pages):
        print("Page: ", i)
        page = pdf.pages[0]

        # Size need to be inverted due to the way PyPDF2 works
        # starting from the bottom of the page
        page.cropbox.upper_left = (0, total_height - A4_HEIGHT * i)
        page.cropbox.lower_right = (
            page.mediabox.width, total_height - A4_HEIGHT * (i + 1))

        output_pdf.add_page(page)

    print("Total Height: ", total_height)
    print("Number of Pages: ", number_of_pages)

    return output_pdf


def save_as_a4(output_pdf, output_path):
    with open(output_path, 'wb') as output_file:
        output_pdf.write(output_file)


def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if output_path:
            pdf = split_pdf(file_path)
            save_as_a4(pdf, output_path)
            status_label.config(text="PDF Split and Saved Successfully")


# GUI
root = tk.Tk()
root.geometry("300x150")
root.title("PDF Viezzer")

instructions_label = tk.Label(root, text="Select a PDF file to split:")
instructions_label.pack(pady=10)

split_button = tk.Button(root, text="Split PDF", command=choose_file)
split_button.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack(pady=10)

root.mainloop()
