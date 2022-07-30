with open('data.txt') as f:
    file_data = f.readlines()

data = []
for s in file_data:
    data.append(int(s))

count = 0
m = -20000
for i in range(len(data) - 1):
    if data[i] % 3 == 0 or data[i + 1] % 3 == 0:
        count += 1
        m = max(m, data[i] + data[i + 1])
print(count, m)
