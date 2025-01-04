import tkinter as tk
import random
import time

root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("500x400")

# Title Label
title_label = tk.Label(root, text="Typing Speed Test", font=("Helvetica", 16, "bold"))
title_label.pack(pady=20)

# Sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "Practice makes perfect, so keep typing.",
    "Typing tests are a fun way to improve your skills.",
    "Stay focused and type as quickly as you can."
]

# Sentence Label
sentence_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=400)
sentence_label.pack(pady=20)

# Function to Display Random Sentence
def display_random_sentence():
    global current_sentence
    current_sentence = random.choice(sentences)
    sentence_label.config(text=current_sentence)

# Initialize with First Sentence
current_sentence = ""
display_random_sentence()

# Input Box
input_box = tk.Entry(root, font=("Helvetica", 12), width=40)
input_box.pack(pady=10)
input_box.focus_set()  # Automatically focus on the input box

# Timing Variables
start_time = None

# Start Timer
def start_timer(event):
    global start_time
    if start_time is None:  # Start timing only once
        start_time = time.time()

# Stop Timer and Calculate Results
def stop_timer(event):
    global start_time
    if start_time is not None:
        elapsed_time = time.time() - start_time
        user_input = input_box.get()
        calculate_results(user_input, elapsed_time)

# Calculate Typing Speed and Accuracy
def calculate_results(user_input, elapsed_time):
    global start_time
    # Calculate WPM
    word_count = len(current_sentence.split())
    words_per_minute = (word_count / elapsed_time) * 60

    # Calculate Accuracy
    correct_chars = sum(1 for i, char in enumerate(user_input) if i < len(current_sentence) and char == current_sentence[i])
    total_chars = len(current_sentence)
    accuracy = (correct_chars / total_chars) * 100

    # Display Results
    result_label.config(text=f"WPM: {words_per_minute:.2f}, Accuracy: {accuracy:.2f}%")

    # Reset Input and Timer
    input_box.delete(0, tk.END)
    display_random_sentence()
    start_time = None

# Reset Test
def reset_test():
    global start_time
    input_box.delete(0, tk.END)  # Clear the input box
    display_random_sentence()  # Display a new random sentence
    result_label.config(text="")  # Clear the results
    start_time = None
    input_box.focus_set()  # Set focus back to the input box

# Bind Events
input_box.bind("<KeyPress>", start_timer)  # Start timer on any key press
input_box.bind("<Return>", stop_timer)  # Stop timer and calculate results on Enter

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# Restart Button
restart_button = tk.Button(root, text="Restart", font=("Helvetica", 12), command=reset_test)
restart_button.pack(pady=20)

# Start the Main Loop
root.mainloop()
