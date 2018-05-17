from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import time

def Inter(C1, C2):
    if C1.x+C1.r>=C2.x-C2.r and C1.x-C1.r<=C2.x+C2.r and C1.y+C1.r>=C2.y-C2.r and C1.y-C1.r<=C2.y+C2.r:
        return True
    else:
        return False
dir
#classes
class Player:
    def __init__(self, x=0, y=0, dx=0, dy=0, dir='', r=10, color='black', reload=0, alive=True):
        self.x=x
        self.y=y
        self.color=color
        self.dx=dx
        self.dy=dy
        self.dir=dir
        self.r=r
        self.reload=reload
        self.alive=alive
        #syst
        self.v=1
        self.inrage=False
        self.timerage=0
    def step(self):
        if self.alive:
            self.x+=self.dx
            self.y+=self.dy
            if self.reload>0:
                self.reload-=1
            if self.timerage>0:
                self.timerage-=1
                if self.timerage<=0:
                    self.v/=2
                    self.dx/=2
                    self.dy/=2
                    self.inrage=False
                    self.reload=360
    def draw(self, canv):
        canv.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.color)
        if self.reload>0:
            canv.create_arc(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, start=90, extent=self.reload, fill='lightblue')
    def inter(self, C):
        if not self.inrage and C.inrage:
            self.death
        elif self.inrage and not C.inrage:
            C.death
        else:
            self.dx*=-1
            self.dy*=-1
            C.dx*=-1
            C.dy*=-1
    def death(self):
        self.alive=False
        self.dx=0
        self.dy=0
        self.x=-50
        self.y=-50

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
        P.append(Player(30, 30, 1.5, 0, 'd', 10, 'Blue', ))
        P.append(Player(1560, 800, -1.5, 0, 'a', 10, 'Red'))
    
    gameloop=True
    nexttime=time.time()+ticktime
    while gameloop:
        while time.time()<nexttime:
            pass
        nexttime=time.time()+ticktime
        
        canv.delete('all')
        for i in P:
            for j in P[:]:
                if Inter(i, j):
                    i.inter(j)
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
    if navig=='menu':
        if 600<=x<=1000 and 80<=y<=230:
            navig='game'
            Game()
        elif 600<=x<=1000 and 260<=y<=410:
            navig='modes'
            Modes()
        elif 600<=x<=1000 and 440<=y<=590:
            navig='stat'
            Statistics()
        elif 600<=x<=1000 and 620<=y<=770:
            navig='opt'
            Options()

def KeyPress(event):
    eks=event.keysym
    if eks=='Escape':
        if askyesno('Exit', 'Do you want to quit?'):
            root.destroy()
    if navig=='game':
        if eks=='w' and P[0].dir!='s':
            P[0].dx=0
            P[0].dy=-1.5*P[0].v
            P[0].dir='w'
        if eks=='a' and P[0].dir!='d':
            P[0].dx=-1.5*P[0].v
            P[0].dy=0
            P[0].dir='a'
        if eks=='s' and P[0].dir!='w':
            P[0].dx=0
            P[0].dy=1.5*P[0].v
            P[0].dir='s'
        if eks=='d' and P[0].dir!='a':
            P[0].dx=1.5*P[0].v
            P[0].dy=0
            P[0].dir='d'
        if eks=='e' and P[0].reload<=0:
            P[0].timerage=100
            P[0].v*=2
            P[0].dx*=P[0].v
            P[0].dy*=P[0].v
            P[0].inrage=True
        #
        if eks=='i' and P[1].dir!='k':
            P[1].dx=0
            P[1].dy=-1.5*P[1].v
            P[1].dir='i'
        if eks=='j' and P[1].dir!='l':
            P[1].dx=-1.5*P[1].v
            P[1].dy=0
            P[1].dir='j'
        if eks=='k' and P[1].dir!='i':
            P[1].dx=0
            P[1].dy=1.5*P[1].v
            P[1].dir='k'
        if eks=='l' and P[1].dir!='j':
            P[1].dx=1.5*P[1].v
            P[1].dy=0
            P[1].dir='l'
        if eks=='o' and P[1].reload<=0:
            P[1].timerage=100
            P[1].v*=2
            P[1].dx*=P[1].v
            P[1].dy*=P[1].v
            P[1].inrage=True
    

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
canv=Canvas(root,width=1590,height=830)
canv.pack()

#binds
root.bind('<KeyPress>', KeyPress)
root.bind('<Motion>', MouseMove)
root.bind('<Button-1>', Button1)

#defs
CreateMenu()

root.mainloop()
