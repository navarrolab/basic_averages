n = int(input())

categories = []
sales = []
total_sales = 0

for _ in range(n):
    line = input().split()
    category = line[0]
    sale = int(line[1])
    categories.append(category)
    sales.append(sale)
    total_sales += sale

# Найдите категорию с максимальными продажами
max_sales = max(sales)
leader_index = sales.index(max_sales)
leader_category = categories[leader_index]

# Рассчитайте её долю в процентах
share = (max_sales / total_sales) * 100

# Выведите результат в формате: "Лидер: {название}, доля {доля:.2f}%"
print(f"Лидер: {leader_category}, доля {share:.2f}%")