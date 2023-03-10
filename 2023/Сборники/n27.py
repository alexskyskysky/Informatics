with open("C:\\ЕГЭ\\ЕГЭ-23\\Сборник 14 вариантов\\Вариант 1\\Задание 27\\27-B.txt", "r") as f:
    n = int(f.readline())
    nums = [int(x) for x in f.readlines()]

k = 107
max_sum = 0
min_length = n
left = right = 0
curr_sum = 0

while right < n:
    curr_sum += nums[right]
    while curr_sum % k != 0 and left < right:
        curr_sum -= nums[left]
        left += 1
    if curr_sum % k == 0 and curr_sum > max_sum:
        max_sum = curr_sum
        min_length = right - left + 1
    elif curr_sum % k == 0 and curr_sum == max_sum:
        min_length = min(min_length, right - left + 1)
    right += 1

print(min_length)
