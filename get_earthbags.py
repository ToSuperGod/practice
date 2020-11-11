
a = [10, 303, 207, 302, 389, 301, 155, 300, 299, 170, 158, 65]  # 自己写输入
count_max = 0  # 可能接到的沙包
for i in range(0, len(a)):  # 统计每个数后比自己小的数的个数
    count = 0
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            count += 1
    a[i] = count
while a:
    num = -1
    flag = 0
    for j in range(0, len(a)):  # 找出数组中的最大数
        if a[j] >= num:
            num = a[j]
            flag = j  # 要弹出数的下标值
    count_max += 1
    for _ in range(flag + 1):  # 弹出最大数和最大数之前的所有数
        a.pop(0)
print(count_max)








