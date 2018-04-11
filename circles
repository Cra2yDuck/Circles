from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import time

#classes
class Player:
    def __init__(self, x, y, color, dx=0, dy=0, r=5, reload=0, alive=True):
        self.x=x
        self.y=y
        self.color=color
        self.dx=dx
        self.dy=dy
        self.r=r
        self.reload=reload
        self.alive=alive
    def step(self):
        if self.alive:
            self.x+=self.dx
            self.y+=self.dy
            if self.reload>0:
                self.reload-=1
    def draw(self, canv):
        canv.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.color)

#defs
def CreateMenu():
    x1=600
    x2=1000
    y=80
    canv.create_rectangle(x1, y, x2, 150+y)
    canv.create_rectangle(x1, 180+y, x2, 330+y)
    canv.create_rectangle(x1, 360+y, x2, 510+y)
    canv.create_rectangle(x1, 540+y, x2, 690+y)
    canv.create_text((x1+x2)//2, y+75, text='Новая игра', font='Arial 54')
    canv.create_text((x1+x2)//2, y+260, text='Режим игры', font='Arial 54')
    canv.create_text((x1+x2)//2, y+435, text='Статистика', font='Arial 54')
    canv.create_text((x1+x2)//2, y+610, text='Настройки', font='Arial 54')

#game
def Game():
    canv.delete('all')
    if mode=='1x1':
        P.append(Player(20, 20, 'Black', 1))
        P.append(Player(1560, 840, 'Red', -1))
    
    gameloop=True
    nexttime=time.time()+ticktime
    while gameloop:
        while time.time()<nexttime:
            pass
        nexttime=time.time()+ticktime
        
        canv.delete('all')
        for i in P:
            print(i.x)
            i.step()
            i.draw(canv)
        canv.update()


#events
def MouseMove(event):
    global butmen1, butmen2, butmen3, butmen4
    x=event.x
    y=event.y
    if navig=='menu':
        if 600<=x<=1000 and 80<=y<=230 and butmen1==False:
            butmen1=True
            canv.create_rectangle(600, 80, 1000, 230, outline='blue')
            canv.create_text(800, 155, text='Новая игра', font='Arial 54', fill='lightblue')
        elif (x<600 or x>1000 or y<80 or y>230) and butmen1==True:
            butmen1=False
            canv.create_rectangle(600, 80, 1000, 230)
            canv.create_text(800, 155, text='Новая игра', font='Arial 54')
        elif 600<=x<=1000 and 260<=y<=410 and butmen2==False:
            butmen2=True
            canv.create_rectangle(600, 260, 1000, 410, outline='blue')
            canv.create_text(800, 340, text='Режим игры', font='Arial 54', fill='lightblue')
        elif (x<600 or x>1000 or y<260 or y>410) and butmen2==True:
            butmen2=False
            canv.create_rectangle(600, 260, 1000, 410)
            canv.create_text(800, 340, text='Режим игры', font='Arial 54')
        elif 600<=x<=1000 and 440<=y<=590 and butmen3==False:
            butmen3=True
            canv.create_rectangle(600, 440, 1000, 590, outline='blue')
            canv.create_text(800, 515, text='Статистика', font='Arial 54', fill='lightblue')
        elif (x<600 or x>1000 or y<440 or y>590) and butmen3==True:
            butmen3=False
            canv.create_rectangle(600, 440, 1000, 590)
            canv.create_text(800, 515, text='Статистика', font='Arial 54')
        elif 600<=x<=1000 and 620<=y<=770 and butmen4==False:
            butmen4=True
            canv.create_rectangle(600, 620, 1000, 770, outline='blue')
            canv.create_text(800, 690, text='Настройки', font='Arial 54', fill='lightblue')
        elif (x<600 or x>1000 or y<620 or y>770) and butmen4==True:
            butmen4=False
            canv.create_rectangle(600, 620, 1000, 770)
            canv.create_text(800, 690, text='Настройки', font='Arial 54')

def Button1(event):
    global navig
    x=event.x
    y=event.y
    if 600<=x<=1000 and 80<=y<=230:
        Game()
        navig='game'
    elif 600<=x<=1000 and 260<=y<=410:
        Modes()
        navig='modes'
    elif 600<=x<=1000 and 440<=y<=590:
        Statistics()
        navig='stat'
    elif 600<=x<=1000 and 620<=y<=770:
        Options()
        navig='opt'

def KeyPress(event):
    eks=event.keysym
    if eks=='Escape':
        if askyesno('Exit', 'Do you want to quit?'):
            root.destroy()

#variables
navig='menu'
mode='1x1'
butmen1=False
butmen2=False
butmen3=False
butmen4=False
ticktime=0.01

P=[]

#root
root=Tk()
canv=Canvas(root,width=1580,height=860)
canv.pack()

#binds
root.bind('<KeyPress>', KeyPress)
root.bind('<Motion>', MouseMove)
root.bind('<Button-1>', Button1)

#defs
CreateMenu()

root.mainloop()
