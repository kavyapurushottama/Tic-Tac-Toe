from tkinter import *
import random

def next(row,column):
    global player
    if board[row][column]['text']=="" and winner() is False:
        if player==players[0]:
            board[row][column]['text']=player
            if winner() is False:
                player=players[1]
                label.config(text=(players[1]+"'s"+" Turn"))
            elif winner() is True:
                label.config(text=(players[0]+" Wins"))
            elif winner()=="Tie":
                label.config(text="Tie!")
        else:
            board[row][column]['text']=player
            if winner() is False:
                player=players[0]
                label.config(text=(players[0]+"'s"+" Turn"))
            elif winner() is True:
                label.config(text=(players[1]+" Wins"))
            elif winner()=="Tie":
                label.config(text="Tie!")
def new_game():
    global player
    player=random.choice(players)
    label.config(text=player+"'s"+" Turn")
    for row in range(3):
        for column in range(3):
            board[row][column].config(text='',bg="white")
def empty():
    spaces=9
    for row in range(3):
        for column in range(3):
            if board[row][column]['text']!="":
                spaces-=1
    if spaces==0:
        return False
    else:
        return True
def winner():
    for row in range(3):
        if board[row][0]['text']==board[row][1]['text']==board[row][2]['text']!="" :
            board[row][0].config(bg='green')
            board[row][1].config(bg='green')
            board[row][2].config(bg='green')
            return True
    for column in range(3):
        if board[0][column]['text']==board[1][column]['text']==board[2][column]['text']!="" :
            board[0][column].config(bg='green')
            board[1][column].config(bg='green')
            board[2][column].config(bg='green')
            return True
    if board[0][0]['text']==board[1][1]['text']==board[2][2]['text']!="":
        board[0][0].config(bg='green')
        board[1][1].config(bg='green')
        board[2][2].config(bg='green')
        return True
    elif board[0][2]['text']==board[1][1]['text']==board[2][0]['text']!="":
        board[0][2].config(bg='green')
        board[1][1].config(bg='green')
        board[2][0].config(bg='green')
        return True
    elif empty() is False:
        return "Tie"
    else: 
        return False
     

window=Tk()
window.title("Tic Tac Toe")
players=["X","O"]
player=random.choice(players)
board=[[0,0,0],[0,0,0],[0,0,0]]
label=Label(text=player+"'s" +" Turn",font=("Arial",30))
label.pack(side="top")

reset=Button(text="reset",command=new_game,font=("Arial",20))
reset.pack(side="bottom")

frame=Frame(window)
frame.pack()
for row in range(3):
    for column in range(3):
        board[row][column]=Button(frame,text="",font=('arial',30),width=5,height=2,command=lambda row=row,column=column:next(row,column))
        board[row][column].grid(row=row,column=column)

window.mainloop()