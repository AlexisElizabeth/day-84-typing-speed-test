import time
from random import choice
from tkinter import *

start_time = 0
trial_text = ""


def random_quote():
    with open("quotes.txt", "r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = choice(all_quotes).split(" - ")[0].split('"')[1]
    return quote


def words_correct(result_list, goal_list):
    correct_words = 0
    for word in result_list:
        if word in goal_list:
            correct_words += 1
    return correct_words


def words_per_minute(total_correct_words, time_in_seconds):
    wpm = total_correct_words / time_in_seconds * 60
    return wpm


def speed_test_start():
    global start_time, trial_text
    entry.delete("1.0", 'end-1c')
    start_time = time.time()
    trial_text = random_quote()
    label.config(text=trial_text, wraplength=500)


def speed_test_end():
    trial_text_list = trial_text.split(" ")
    your_text = entry.get("1.0", 'end-1c')
    your_text_list = your_text.split(" ")
    total_time = time.time() - start_time
    number_correct_words = words_correct(your_text_list, trial_text_list)
    result = words_per_minute(number_correct_words, total_time)
    result_text = f"You typed {number_correct_words} words correctly in {round(total_time, 2)} seconds, " \
                  f"resulting in a typing speed of {round(result, 2)} WPM"
    label.config(text=result_text, wraplength=500)


if __name__ == "__main__":
    window = Tk()
    window.title("Typing Speed Test")
    window.config(padx=50, pady=20, bg="#D3D3D3")

    title_label = Label(text="Typing Speed Test", fg="black", bg="#D3D3D3", font=("Courier", 24))
    title_label.grid(column=1, row=0, columnspan=2)

    label = Label(text="Click to Start the Test", bg="#D3D3D3", font=("Courier", 14))
    label.grid(column=1, row=1, columnspan=2)

    entry = Text(width=50, height=3)
    entry.grid(column=1, columnspan=2, row=3)

    start_button = Button(text="Start", command=speed_test_start)
    start_button.grid(column=1, row=4, pady=20)

    end_button = Button(text="End", command=speed_test_end)
    end_button.grid(column=2, row=4, pady=20)

    window.mainloop()


