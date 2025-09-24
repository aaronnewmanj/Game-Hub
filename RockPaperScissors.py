from tkinter import *
import random

def open_game1():
    win = Toplevel()   # <-- not Tk()
    win.title("Rock Paper Scissors")

    choices = ["Rock", "Paper", "Scissors"]
    youscore = 0
    comscore = 0

    # ---- Functions (use closure to keep scores accessible) ----
    def play(selection, you, computer, result, yscore, cscore):
        nonlocal youscore, comscore
        computer_choice = random.choice(choices)

        you.delete(0, END)
        computer.delete(0, END)
        result.delete(0, END)
        yscore.delete(0, END)
        cscore.delete(0, END)

        you.insert(0, selection)
        computer.insert(0, computer_choice)

        if selection == computer_choice:
            result.insert(0, "Tie")
        elif (selection == "Rock" and computer_choice == "Scissors") or \
             (selection == "Paper" and computer_choice == "Rock") or \
             (selection == "Scissors" and computer_choice == "Paper"):
            result.insert(0, "You Won")
            youscore += 1
        else:
            result.insert(0, "Computer Won")
            comscore += 1

        yscore.insert(0, youscore)
        cscore.insert(0, comscore)

    def clear(you, computer, result, yscore, cscore):
        nonlocal youscore, comscore
        youscore, comscore = 0, 0
        for entry in (you, computer, result, yscore, cscore):
            entry.delete(0, END)
        yscore.insert(0, 0)
        cscore.insert(0, 0)

    # ---- UI ----
    choice_label = Label(win, text="Your choice:")
    choice_label.grid(row=3, column=0)
    choice_display = Entry(win)
    choice_display.grid(row=3, column=1)

    computer_choice_label = Label(win, text="Computer's choice:")
    computer_choice_label.grid(row=4, column=0)
    computer_choice_display = Entry(win)
    computer_choice_display.grid(row=4, column=1)

    result_label = Label(win, text="Round Result:")
    result_label.grid(row=5, column=0)
    result_display = Entry(win)
    result_display.grid(row=5, column=1)

    score_label = Label(win, text="Your Score:")
    score_label.grid(row=7, column=0)
    score_display = Entry(win, justify="center")
    score_display.grid(row=8, column=0)

    computer_score_label = Label(win, text="Computer's Score:")
    computer_score_label.grid(row=7, column=1)
    computer_score_display = Entry(win, justify='center')
    computer_score_display.grid(row=8, column=1)

    fontsize = 20
    Button(win, text="Rock", font=("Helvetica", fontsize),
           command=lambda: play("Rock", choice_display, computer_choice_display, result_display, score_display, computer_score_display)).grid(row=0, column=0)
    Button(win, text="Paper", font=("Helvetica", fontsize),
           command=lambda: play("Paper", choice_display, computer_choice_display, result_display, score_display, computer_score_display)).grid(row=0, column=1)
    Button(win, text="Scissors", font=("Helvetica", fontsize),
           command=lambda: play("Scissors", choice_display, computer_choice_display, result_display, score_display, computer_score_display)).grid(row=0, column=2)
    Button(win, text="Clear", font=("Helvetica", fontsize),
           command=lambda: clear(choice_display, computer_choice_display, result_display, score_display, computer_score_display)).grid(row=9, column=1)
