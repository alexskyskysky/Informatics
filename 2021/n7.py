# Вариант 1 (2021)
x = 490
y = 1024  # x, y - длина и ширина изображения
N_Kb = 490  # размер в килобайтах
N_bit = N_Kb * 1024 * 8  # размер в битах
b = N_bit // (x * y)  # сколько бит на один пиксель
colors = 2 ** b  # сколько цветов можно закодировать
print(colors)
