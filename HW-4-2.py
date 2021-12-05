data = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = [el for num, el in enumerate(data) if data[num] > data[num - 1] if num >= 1]
print(new)
