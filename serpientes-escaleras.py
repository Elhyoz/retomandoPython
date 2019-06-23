
import random as rnd

'''Comentario de cambio para commit'''
meta = 64


A = 0
B = 0

turno = 0
while not(A>meta or B>meta):
    r = turno%2

    if (r==0):
        dado = int(rnd.random()*6)+1
        A = A + dado
        if (A==4 or A==9):
            A = A + 3
       

    if (r>0):
        dado = int(rnd.random()*6)+1
        B = B + dado
        if (B==4 or B==9):
            B = B + 3
       

    turno = turno +1

if (A>B):
    gana = 1
else:
    gana = 2


print('casilla final A: ', A)
print('casilla final B: ', B)
print('ganó el jugador: ',gana)