n = input()#ввод строки

x = len(n) // 2#длина троки делённая на 2
if len(n) % 2 == 0:#условие
    print(n[x:] + n[:x])# print 1

else:
    print(n[x + 1:] + n[:x+ 1])#print по другому


import turtle
t=turtle.Pen()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.reset()
for s in range(1,9):
    t.forward(100)
    t.left(225)
