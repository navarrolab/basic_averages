data = [2, 4, 6, 8]
mean = sum(data)/len(data)
var_list = []
for x in data:
    var_list.append(((x - mean)**2))
var = sum(var_list)/(len(var_list)-1)
std = var**0.5
print(f'''Среднее: {mean:.2f}
Дисперсия: {var:.2f}
Стандартное отклонение: {std:.2f}''')