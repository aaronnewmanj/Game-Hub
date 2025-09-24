from tkinter import *
import random

#make loop for generating buttons
#make a condition satisdied whenever the dice roll total is met

def open_game2():
    win = Toplevel()   
    win.title("Shut The Box Game")

    total = 0
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    diceRoll=0

    def can_make_sum(numbers, target):
        dp = [False] * (target + 1)
        dp[0] = True  

        for num in numbers:
            for i in range(target, num - 1, -1):  
                if dp[i - num]:
                    dp[i] = True

        return dp[target]
    
    
    

    def check_result(result):
        nonlocal total
        nonlocal diceRoll
        if len(numbers)==0 and result.get()=="":
            result.insert(0, "YOU WON")
        if total>diceRoll:
            result.insert(0, "Can't do that.")

    def lost_check(result):
        nonlocal numbers, diceRoll
        if not can_make_sum(numbers, diceRoll):
            result.delete(0, END)
            result.insert(0, "YOU LOST")

    def press_action(flip, value, result):
        nonlocal total
        nonlocal numbers

        result.delete(0, END)
        
        if flip.get() == "FLIPPED":
            flip.delete(0, END)
            total -= value
            numbers.append(value)
        else:
            flip.insert(0, "FLIPPED")
            total += value
            numbers.remove(value)
        check_result(result)
        lost_check(result)

        


    def press1(flip, result):
        value = 1
        press_action(flip, value, result)
        
    def press2(flip, result):
        value = 2
        press_action(flip, value, result)
        

    def press3(flip, result):
        value = 3
        press_action(flip, value, result)
        

    def press4(flip, result):
        value = 4
        press_action(flip, value, result)
        

    def press5(flip, result):
        value = 5
        press_action(flip, value, result)

    def press6(flip, result):
        value = 6
        press_action(flip, value, result)

    def press7(flip, result):
        value = 7
        press_action(flip, value, result)
        

    def press8(flip, result):
        value = 8
        press_action(flip, value, result)

    def press9(flip, result):
        value = 9
        press_action(flip, value, result)
        


    def roll(dice, result):
        nonlocal total
        total=0
        dice.delete(0, END)
        result.delete(0,END)
        nonlocal diceRoll
        diceRoll=random.randint(2,12)
        dice.insert(0, diceRoll)
        lost_check(result)
        

    def clear(flip1, flip2, flip3, flip4, flip5, flip6, flip7, flip8, flip9, dice, result):
        nonlocal total
        nonlocal numbers
        numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9]
        total=0
        dice.delete(0, END)
        flip1.delete(0, END)
        flip2.delete(0, END)
        flip3.delete(0, END)
        flip4.delete(0, END)
        flip5.delete(0, END)
        flip6.delete(0, END)
        flip7.delete(0, END)
        flip8.delete(0, END)
        flip9.delete(0, END)
        result.delete(0, END)








    fontsize=30 

    button1 = Button(win, fg="black", text="1", font=("Helvetica", fontsize), width=10, height=10, command=lambda: press1(isFlipped1, resultDisplay))
    button1.grid(column=0, row=0, columnspan=1)
    isFlipped1= Entry(win, justify="center")
    isFlipped1.grid(column=0, row=1, columnspan=1)

    button2 = Button(win, fg="black", text="2", font=("Helvetica", fontsize), width=10, height=10, command=lambda: press2(isFlipped2, resultDisplay))
    button2.grid(column=1, row=0, columnspan=1)
    isFlipped2= Entry(win, justify="center")
    isFlipped2.grid(column=1, row=1, columnspan=1)

    button3 = Button(win, fg="black", text="3", font=("Helvetica", fontsize), width=10, height=10, command=lambda: press3(isFlipped3, resultDisplay))
    button3.grid(column=2, row=0, columnspan=1)
    isFlipped3= Entry(win, justify="center")
    isFlipped3.grid(column=2, row=1, columnspan=1)

    button4 = Button(win, fg="black", text="4", font=("Helvetica", fontsize), width=10, height=10, command=lambda: press4(isFlipped4, resultDisplay))
    button4.grid(column=3, row=0, columnspan=1)
    isFlipped4= Entry(win, justify="center")
    isFlipped4.grid(column=3, row=1, columnspan=1)

    button5 = Button(win, fg="black", text="5", font=("Helvetica", fontsize), width=10, height=10, command=lambda: press5(isFlipped5, resultDisplay))
    button5.grid(column=4, row=0, columnspan=1)
    isFlipped5= Entry(win, justify="center")
    isFlipped5.grid(column=4, row=1, columnspan=1)

    button6 = Button(win, fg="black", text="6", font=("Helvetica", fontsize), width=10, height=10, command=lambda: press6(isFlipped6, resultDisplay))
    button6.grid(column=5, row=0, columnspan=1)
    isFlipped6= Entry(win, justify="center")
    isFlipped6.grid(column=5, row=1, columnspan=1)

    button7 = Button(win, fg="black", text="7", font=("Helvetica", fontsize), width=10, height=10, command=lambda: press7(isFlipped7, resultDisplay))
    button7.grid(column=6, row=0, columnspan=1)
    isFlipped7= Entry(win, justify="center")
    isFlipped7.grid(column=6, row=1, columnspan=1)

    button8 = Button(win, fg="black", text="8", font=("Helvetica", fontsize), width=10, height=10, command=lambda: press8(isFlipped8, resultDisplay))
    button8.grid(column=7, row=0, columnspan=1)
    isFlipped8= Entry(win, justify="center")
    isFlipped8.grid(column=7, row=1, columnspan=1)

    button9 = Button(win, fg="black", text="9", font=("Helvetica", fontsize), width=10, height=10, command=lambda: press9(isFlipped9, resultDisplay))
    button9.grid(column=8, row=0, columnspan=1)
    isFlipped9= Entry(win, justify="center")
    isFlipped9.grid(column=8, row=1, columnspan=1)

    rollButton = Button(win, fg="green", text="Roll", font=("Helvetica", fontsize), width=10, height=2, command=lambda: roll(diceDisplay, resultDisplay))
    rollButton.grid(column=8, row=3, columnspan=1)

    clearButton = Button(win, fg="red", text="Clear", font=("Helvetica", fontsize), width=10, height=2, command=lambda: clear(isFlipped1, isFlipped2, isFlipped3, isFlipped4, isFlipped5, isFlipped6, isFlipped7, isFlipped8, isFlipped9, diceDisplay, resultDisplay))
    clearButton.grid(column=8, row=5, columnspan=1)

    diceLabel = Label(win, text="Dice Roll:")
    diceLabel.grid(column=4, row=2, columnspan=1)

    diceDisplay = Entry(win, justify="center")
    diceDisplay.grid(column=4, row=3, columnspan=1)

    resultDisplay = Entry(win, justify="center")
    resultDisplay.grid(column=4, row=4, columnspan=1)




    win.mainloop()

    #add ability to see if youve lost
    #add checker to see if math is valid
