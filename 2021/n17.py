# Вариант 1 (2021)
count = 0
max = 1006
for x in range(1007, 8011):
    if x % 6 == 0 and x % 4 != 0 and x % 5 != 0 and x % 9 != 0 and x % 13 != 0:
        count += 1
        if x > max:
            max = x
print(count, max)
