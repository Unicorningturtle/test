from tkinter import *
import random

root = Tk()

position = []

#def move(x,y):



room_map = []
entities = {
"player": 1, "mimic": 2, "sceleton": 6, "tnt": 6, "slime": 8, "door": 1, "boss":1}
names = ["Alex", "Nik", "Ben", "Rober", "Artem"]

name = Label(root, text = names[random.randint(0, len(names)-1)]).grid(row = 0, column = 0, columnspan = 5)
hp = 3; health = Label(root, text = "Здоровье:"+str(hp))
cn = 0; coins = Label(root, text = "Деньги:"+str(cn))
w = "меч"; weapon = Label(root, text = "Оружие:"+w)
at = 1; attack = Label(root, text = "Урон:"+str(at))
kt = 15; krit = Label(root, text = "Шанс крита:"+str(kt)+"%")
v1 = Button(root, text = "бить")
v2 = Button(root, text = "бежать")
turn = 1; time = Label(root, text = "Ход:"+str(turn))
health.grid(row=1, column = 0, columnspan = 5)
coins.grid(row=2, column = 0, columnspan = 5)
krit.grid(row=3, column = 0, columnspan = 5)
weapon.grid(row=4, column = 0, columnspan = 5)
attack.grid(row=5, column = 0, columnspan = 5)
v1.grid(row=6, column = 0, columnspan = 5)
v2.grid(row=7, column = 0, columnspan = 5)
time.grid(row=8, column = 0, rowspan = 2, columnspan = 5)



for i in range(10):
    room_map.append([])
    for j in range(10):
        r = random.randint(0, 100)
        if r < 1.5 and entities["player"]>0:
            color = "blue"
            entities["player"] -= 1
            position = [i, j]
        elif r > 1.5 and r < 4.5 and entities["mimic"]>0:
            color = "gold"
            entities["mimic"] -= 1
        elif r > 4.5 and r < 13.5 and entities["sceleton"]>0:
            color = "grey"
            entities["sceleton"] -= 1
        elif r > 13.5 and r < 22.5 and entities["tnt"]>0:
            color = "red"
            entities["tnt"] -= 1
        elif r > 22.5 and r < 34.5 and entities["slime"]>0:
            color = "pink"
            entities["slime"] -= 1
        elif r > 34.5 and r < 36 and entities["boss"]>0:
            color = "purple"
            entities["boss"] -= 1
        elif r > 36 and r < 37.5 and entities["door"]>0:
            color = "brown"
            entities["door"] -= 1
        else: color = "green"
        room_map[i].append(Button(root, bg = color))
for i in range(10):
    for j in range(10):
        room_map[i][j].grid(row = i, column = j+5)

root.mainloop()