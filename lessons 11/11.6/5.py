import math

earth_volume = float(1.08321 * 10 ** 12)
radius = float(input('Введите радиус случайной планеты: '))

volume = (4 / 3) * math.pi * (radius ** 3)
ratio = earth_volume/volume

rounted_ratio = round(ratio, 3)

print(f"Объём Земли {'больше' if ratio > 1 else 'меньше'} в {abs(rounted_ratio)} раз")