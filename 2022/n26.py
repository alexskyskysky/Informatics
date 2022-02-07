# Вариант 1 (2022)
Rare = []  # редкие книги
Normal = []  # обычные книги
with open("C:\\ЕГЭ-22\\Сброник 12 вариантов\\Вариант 1\\Задание 26\\26.txt", "r") as f:
    S, N = map(int, f.readline().split())
    for i in range(N):
        book = int(f.readline().strip())
        if book > 3000:
            Rare.append(book)
        else:
            Normal.append(book)

Rare.sort()
Normal.sort()
S -= Rare[0] + Rare[1] + Rare[2]  # в любом случае должно быть 3 редких книги
count = 3
if S <= 0:  # если после 3 редких книг деньги закончились
    print("3, 0")
else:
    max_normal_book = 0
    i = 0
    while S > 0 and i < len(Normal):  # пока есть деньги, покупаем обычные книги
        S -= Normal[i]
        max_normal_book = Normal[i]
        count += 1
        i += 1
    if i == len(Normal):  # если закончились книги
        if S >= 0:  # если при этом остались деньги
            print(count, max_normal_book)
        else:  # если одновременно закончились книги и деньги
            max_normal_book = Normal[i - 2]
            if S + Normal[i - 1] + Normal[i - 2] > Normal[i - 1]:
                max_normal_book = Normal[i - 1]
            print(count - 1, max_normal_book)
    else:  # если книги ещё есть, но закончились деньги
        # пытаемся заменить самую дорогую обычную книгу на книгу ещё дороже
        count -= 1
        S += Normal[i - 1] + Normal[i - 2]
        i -= 1
        while i < len(Normal) and Normal[i] <= S:
            i += 1
        max_normal_book = Normal[i - 1]
        print(count, max_normal_book)
