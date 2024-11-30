import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv', delimiter=';')

# Преобразование всех данных в числовой тип
numeric_columns = open(
    "data.csv", encoding="utf-8").readline().strip().split(";")
for column in numeric_columns:
    data[column] = pd.to_numeric(data[column], errors='coerce')

plt.figure(figsize=(10, 6))
data[numeric_columns].boxplot()
plt.xticks(rotation=45, fontsize=7)
plt.show()
