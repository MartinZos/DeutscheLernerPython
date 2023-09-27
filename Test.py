import tkinter as tk
from tkinter import filedialog
import json
import os
import random

sentences = []

def import_button_clicked():
    global sentences, status_label  # Declare 'sentences' and 'status_label' as global variables
    sentences = []  # Initialize 'sentences' as an empty list

    # Open a file dialog to select a JSON file
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])

    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                # Check if the file is empty
                file_contents = file.read()
                if not file_contents:
                    status_label.config(text="JSON file is empty.", fg="red")
                    return sentences

                # Load JSON data from the selected file into a list
                word_pairs = json.loads(file_contents)

                # Append word pairs to 'sentences' list
                sentences.extend(word_pairs)

                # Extract the file name without the suffix
                file_name_without_extension = os.path.splitext(os.path.basename(file_path))[0]

                status_label.config(text=f".json {file_name_without_extension} loaded successfully", fg="green")
                print(f".json {file_name_without_extension} loaded successfully.")
                return sentences
        except FileNotFoundError:
            status_label.config(text="File not found: " + file_path, fg="red")
            print(f"File not found: {file_path}")
        except json.JSONDecodeError as e:
            status_label.config(text="Error decoding JSON file: " + str(e), fg="red")
            print(f"Error decoding JSON file: {e}")
        except Exception as e:
            status_label.config(text="An error occurred: " + str(e), fg="red")
            print(f"An error occurred: {e}")
    else:
        status_label.config(text="No file selected.", fg="red")
        print("No file selected.")

    return sentences

def clear_window():
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

def start_button_clicked():
    # Check if 'sentences' list is empty
    if not sentences:
        status_label.config(text=".json file not loaded", fg="red")
        return

    # Clear the window
    clear_window()

    # Create a label and entry for entering the number of questions
    num_questions_label = tk.Label(root, text="Enter the number of questions:")
    num_questions_entry = tk.Entry(root)
    submit_button = tk.Button(root, text="Submit", command=lambda: submit_button_clicked(num_questions_entry.get()))

    # Place the widgets on the window
    num_questions_label.pack()
    num_questions_entry.pack()
    submit_button.pack()


# Create the main window
root = tk.Tk()
root.title("Button Window")

# Set the initial size of the window (width x height)
root.geometry("600x400")

# Create and configure buttons with larger size
button_width = 10
button_height = 2
start_button = tk.Button(root, text="Start", command=start_button_clicked, width=button_width, height=button_height)
import_button = tk.Button(root, text="Import", command=import_button_clicked, width=button_width, height=button_height)
quit_button = tk.Button(root, text="Quit", command=root.destroy, width=button_width, height=button_height)

# Create a label for displaying status messages
status_label = tk.Label(root, text="", font=("Helvetica", 12))

# Place the buttons and status label
status_label.pack(pady=20)
start_button.pack()
import_button.pack()
quit_button.pack()

# Start the tkinter main loop
root.mainloop()
