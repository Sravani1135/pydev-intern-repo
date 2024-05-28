import tkinter as tk
from tkinter import messagebox
import random

def Game_Start():
    user_input=entry.get()
    user_choice=user_input.lower()
    if user_choice in ['r',"rock"]:
        user_chooses="rock"
    elif user_choice in ["p","paper"]:
        user_chooses="paper"
    elif user_choice in ["s","scissor"]:
        user_chooses="scissor"
    else:
        r=messagebox.showerror("Sorry, Invalid input! please enter '''r'''/'''p'''/'''s'''/full name of your choice")
        return r

    choices=["rock","paper","scissor"]
    computer_choice=random.choice(choices)
    Result=Winner(user_chooses,computer_choice)
    Display_Final_Result(user_chooses,computer_choice,Result)

def Winner(us,com):
    if us==com:
        return "tie"
    elif (us=="rock" and com=="paper"):
        return "lose"
    elif (us=="paper" and com=="scissor" ):
        return "lose"
    elif (us=="scissor" and com=="rock"):
        return "lose"
    else:
        return "win"

def Display_Final_Result(us,com,result):
    user_emoji="🪨🪨" if us=="rock" else ("📃📃" if us=="paper" else "✂️✂️")
    com_emoji="🪨🪨" if com=="rock" else ("📃📃" if com=="paper" else "✂️✂️")
    if result=="tie":
        display_msg=( f"both choses {us}{(user_emoji)} , \n it's a Tie!!😉" )
    elif result=="win":
        display_msg=(f"you chose {us}{(user_emoji)} but computer chose {com}{(com_emoji)}, \n Hey! you won🥳")
    else:
        display_msg=(f"you chose{ us}{(user_emoji)} but computer chose {com}{(com_emoji)}, \n sorry! you lose☹️")

    messagebox.showinfo("Result",display_msg)


#title of the game
msg_box=tk.Tk()
msg_box.title("Rock🪨Paper📃Scissors✂️")

#user manual
user_manual=tk.Label(msg_box, text="---ENTER---\n'r' / 'rock'--->ROCK🪨\n'p' / 'paper'--->PAPER📃\n's' / 'scissor'--->SCISSORS✂️",font=("caveat",20),bg="light blue")
user_manual.pack()

#user input
entry=tk.Entry(msg_box,font=("Helvetica",16))
entry.pack()


submit_button=tk.Button(msg_box,text="SUBMIT",command=Game_Start,bg="#002366",fg="#89cff0")
submit_button.pack()

msg_box.mainloop()









