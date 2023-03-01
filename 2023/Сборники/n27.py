with open("C:\\ЕГЭ\\ЕГЭ-23\\Сборник 14 вариантов\\Вариант 1\\Задание 27\\27-B.txt", "r") as f:
    n = int(f.readline())
    k = 107
    min_len = 0
    max_sum = 0
    curr_len = 0
    curr_sum = 0
    prefix_sum = [0] * (n + 1)

    for i in range(n):
        num = int(f.readline())
        curr_sum += num
        if curr_sum % k == 0:
            if curr_sum > max_sum:
                max_sum = curr_sum
                min_len = curr_len + 1
            elif curr_sum == max_sum:
                min_len = min(min_len, curr_len + 1)
        elif curr_sum - (curr_sum // k) * k in prefix_sum:
            j = prefix_sum[curr_sum - (curr_sum // k) * k]
            if curr_sum - prefix_sum[curr_sum - (curr_sum // k) * k] > max_sum:
                max_sum = curr_sum - prefix_sum[curr_sum - (curr_sum // k) * k]
                min_len = curr_len - j
            elif curr_sum - prefix_sum[curr_sum - (curr_sum // k) * k] == max_sum:
                min_len = min(min_len, curr_len - j)
        else:
            prefix_sum[curr_sum - (curr_sum // k) * k] = curr_sum
        curr_len += 1
print(min_len)
