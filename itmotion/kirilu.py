import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Ваши данные для одной из зависимостей
x1 = [1, 2, 3, 4, 5]
y1 = [10, 15, 13, 17, 20]

# Выполните линейную регрессию
slope, intercept, r_value, p_value, std_err = linregress(x1, y1)

# Создайте массив значений для аппроксимированной линии
x_fit = np.linspace(min(x1), max(x1), 100)
y_fit = intercept + slope * x_fit

# Постройте исходные данные
plt.plot(x1, y1, label='1 риска', color='green')

# Постройте аппроксимированную линию
plt.plot(x_fit, y_fit, label=f'Линейная аппроксимация, R^2={r_value**2:.2f}', color='blue', linestyle='--')

# Добавьте легенду для обозначения зависимостей
plt.legend()

# Настройте метки осей и заголовок графика
plt.xlabel('e')
plt.ylabel('M')
plt.title('Аппроксимация линейной регрессией')

# Отобразите график
plt.show()
