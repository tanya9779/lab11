'''
Игра с 2 целями
'''
from random import randrange as rnd, choice
from tkinter import *
import math
 
#print (dir(math))
 
import time
root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg = 'white')
canv.pack(fill=BOTH,expand=1)


"""
Класс ball описывает мяч. 
"""
class ball():

    def __init__(self,x=40,y=450):
        """
         Конструктор класса ball
    
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue','green','red','brown'])
        self.id = canv.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.color)
        self.live = 30
         
    def set_coords(self):
        canv.coords(self.id, self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r)
         
    def move(self):
        """
        Метод move описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        #I FIX IT
        self.x += self.vx
        self.y -= self.vy
        self.vy-=self.r*0.1 # чем тяжелее ядро, тем сильнее сила притяжения
        self.set_coords()


    def hittest(self,ob):
        """
        Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте ob.
        Args:
            ob: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """

        #I FIX IT
        dist=math.sqrt( (self.x-ob.x)**2+(self.y-ob.y)**2)
        if dist<self.r+ob.r:
            return True
        return False

"""
Класс gun описывает пушку. 
"""         
class gun():
    def __init__(self):
        #I FIX IT
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7)

    def fire2_start(self,event):
        self.f2_on = 1
 
    def fire2_end(self,event):
        """
        Выстрел мячом при отпускании кнопки мыши. Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y)/(event.x-new_ball.x))
        new_ball.vx = self.f2_power*math.cos(self.an)
        new_ball.vy = -self.f2_power*math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10
 
 
    def targetting (self,event=0):
        """
        Прицеливание. В зависимости от положения мыши
        """

        if event:
            self.an = math.atan((event.y-450)/(event.x-20))    
        if self.f2_on:
            canv.itemconfig(self.id,fill = 'orange')
        else:
            canv.itemconfig(self.id,fill = 'black')
        canv.coords(self.id, 20, 450, 20 + max(self.f2_power, 20) * math.cos(self.an), 450 + max(self.f2_power, 20) * math.sin(self.an))
         

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id,fill = 'orange')
        else:
            canv.itemconfig(self.id,fill = 'black')
        
"""
Класс target описывает цель. 
""" 
class target():

    def __init__(self):
        #I FIX IT
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0,0,0,0)
        self.id_points = canv.create_text(30,30,text = self.points,font = '28')
        self.new_target()
         
    def new_target(self):
        """
        Инициализация новой цели
        """
        x = self.x = rnd(600,780)
        y = self.y = rnd(300,550)
        r = self.r = rnd(2,50)
        color = self.color = choice(['blue','green','red','brown'])
        canv.coords(self.id, x-r,y-r,x+r,y+r)
        canv.itemconfig(self.id, fill = color)
         
    def hit(self,points = 1):
        """
        Попадание шарика в цель
        """
        canv.coords(self.id,-10,-10,-10,-10)
        self.points += points
        canv.itemconfig(self.id_points, text = self.points)
         

t1 = target()
t2 = target()
screen1 = canv.create_text(400,300, text = '',font = '28')
g1 = gun()
bullet = 0
balls = []
 
 
def new_game(event=''):
    global gun, t1, screen1, balls, bullet
    t1.new_target()
    t2.new_target()    # SECOND TARGET
    bullet = 0
    balls = []
    canv.bind('<Button-1>',g1.fire2_start)
    canv.bind('<ButtonRelease-1>',g1.fire2_end)
    canv.bind('<Motion>',g1.targetting)
 
    z = 0.03
    t1.live = 1
    t2.live = 1
    while t1.live or t2.live or balls:
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canv.itemconfig(screen1, text = 'Вы уничтожили цель1 за ' + str(bullet) + ' выстрелов')
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
                canv.itemconfig(screen1, text = 'Вы уничтожили цель2 за ' + str(bullet) + ' выстрелов')
            if not (t1.live or t2.live):
                canv.bind('<Button-1>','')
                canv.bind('<ButtonRelease-1>','')

        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text = '')
    canv.delete(gun)
    root.after(750,new_game)

new_game()   
 
mainloop()

