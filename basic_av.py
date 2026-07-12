import pandas as pd
import numpy as np

import pandas as pd
import numpy as np

# Данные о зарплатах (с выбросом)
salaries = [30, 35, 32, 40, 32, 28, 27, 27, 27, 32, 31, 30, 32, 500]
df = pd.DataFrame({'salary': salaries})

print("=== Основные средние ===")
print(f"Среднее арифметическое: {df['salary'].mean():.1f} тыс. руб.")
print(f"Медиана: {df['salary'].median():.1f} тыс. руб.")
print(f"Мода: {df['salary'].mode().values} тыс. руб.")

# Данные для взвешенного среднего
print("\n=== Взвешенное среднее ===")
scores = {'subject': ['Математика', 'Физика', 'Литература'],
          'grade': [5, 4, 3],
          'weight': [0.5, 0.3, 0.2]}
df_scores = pd.DataFrame(scores)

weighted_avg = np.average(df_scores['grade'], weights=df_scores['weight'])
print(f"Взвешенное среднее: {weighted_avg:.1f}")