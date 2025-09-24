import tkinter as tk 
from RockPaperScissors import *
from ShutTheBox import *
from CatchTheDots import *

main_win = Tk()
main_win.title("Game Hub")

fontsize = 20

game1 = ("Rock Paper Scissors", open_game1)
game2 = ("Shut-the-box", open_game2)
game3 = ("Avoid-the-Dots", open_game3)


game_list = [game1, game2, game3]

# Button to open Rock Paper Scissors

for title, function in game_list:
    btn = tk.Button(main_win, text=title, command=function, width=50, height=5)
    btn.pack(pady=5)

main_win.mainloop()
 

