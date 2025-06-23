import math

def sphereArea(r):
    s = 4 * math.pi * r ** 2
    print(s)

def sphereVolume(r):
    s = 4/3 * math.pi * r ** 3
    print(s)

s = 0
v = 0

r = float(input('Введите обьём: '))

sphereArea(r)
sphereVolume(r)