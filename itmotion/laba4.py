import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

h = 0.7
T_sr_updown= [4.6, 3.4, 2.74, 2.43, 5.66, 4.03, 3.24, 2.81, 6.52, 4.89, 3.88, 3.36, 8.25, 5.59, 4.34, 3.81, 8.9, 6.24, 5.22, 4.44, 9.89, 7.29, 5.77, 5.0]
a = []
for i in range(len(T_sr_updown)):
    a.append((2 * h) / (T_sr_updown[i] ** 2))


a2_riski = a[4:8]
a3_riski= a[8:12]
a4_riski = a[12:16]
a5_riski = a[16:20]
a6_riski = a[20:]


d = 0.046
E_uglovoe_1 = []
E_uglovoe_2 = []
E_uglovoe_3 = []
E_uglovoe_4 = []
E_uglovoe_5 = []
E_uglovoe_6 = []
for q in range(4):
    E_uglovoe_1.append((2 * a[q]) / d )
    E_uglovoe_2.append((2 * a2_riski[q]) / d )
    E_uglovoe_3.append((2 * a3_riski[q]) / d )
    E_uglovoe_4.append((2 * a4_riski[q]) / d )
    E_uglovoe_5.append((2 * a5_riski[q]) / d )
    E_uglovoe_6.append((2 * a6_riski[q]) / d )


g = 9.82
m_with_one = 0.267
m_with_two = 0.314
m_with_three = 0.361
m_with_four = 0.408
a1_m = [a[0], a[4], a[8], a[12], a[16], a[20]]
a2_m = [a[1], a[5], a[9], a[13], a[17], a[21]]
a3_m = [a[2], a[5], a[10], a[14], a[18], a[22]]
a4_m = [a[3], a[6], a[11], a[15], a[19], a[23]]
M1 = []
M2 = []
M3 = []
M4 = []
for i in range(6):
    M1.append((m_with_one * d * (g - a1_m[i])) / 2)
    M2.append((m_with_two * d * (g - a2_m[i])) / 2)
    M3.append((m_with_three * d * (g - a3_m[i])) / 2)
    M4.append((m_with_four * d * (g - a4_m[i])) / 2)



# for grafic

M1_riska = [M1[0], M2[0], M3[0], M4[0]]
M2_riska = [M1[1], M2[1], M3[1], M4[1]]
M3_riska = [M1[2], M2[2], M3[2], M4[2]]
M4_riska = [M1[3], M2[3], M3[3], M4[3]]
M5_riska = [M1[4], M2[4], M3[4], M4[4]]
M6_riska = [M1[5], M2[5], M3[5], M4[5]]


## REAL GRAFIC

# Создайте данные для первой зависимости
y1 = M1_riska
x1 = E_uglovoe_1

slope, intercept, r_value, p_value, std_err = linregress(x1, y1)

x_fit = np.linspace(min(x1), max(x1), 100)
y_fit = intercept + slope * x_fit


y2 = M2_riska
x2 = E_uglovoe_2

slope, intercept, r_value, p_value, std_err = linregress(x2, y2)

x_fit_2 = np.linspace(min(x2), max(x2), 100)
y_fit_2 = intercept + slope * x_fit_2




y3 = M3_riska
x3 = E_uglovoe_3

slope, intercept, r_value, p_value, std_err = linregress(x3, y3)

x_fit3 = np.linspace(min(x3), max(x3), 100)
y_fit3 = intercept + slope * x_fit3



y4 = M4_riska
x4 = E_uglovoe_4

slope, intercept, r_value, p_value, std_err = linregress(x4, y4)

x_fit4 = np.linspace(min(x4), max(x4), 100)
y_fit4 = intercept + slope * x_fit4




y5 = M5_riska
x5 = E_uglovoe_5

slope, intercept, r_value, p_value, std_err = linregress(x5, y5)

x_fit5 = np.linspace(min(x5), max(x5), 100)
y_fit5 = intercept + slope * x_fit5



y6 = M1_riska
x6 = E_uglovoe_6

slope, intercept, r_value, p_value, std_err = linregress(x6, y6)

x_fit6 = np.linspace(min(x6), max(x6), 100)
y_fit6 = intercept + slope * x_fit6



# Постройте первую зависимость (красная линия)
plt.plot(x_fit, y_fit, label='1 риска', color='green')

plt.plot(x_fit_2, y_fit_2, label='2 риска', color='blue')


plt.plot(x_fit3, y_fit3, label='3 риска', color='pink')
plt.plot(x_fit4, y_fit4, label='4 риска', color='orange')
plt.plot(x_fit5, y_fit5, label='5 риска', color='brown')
plt.plot(x_fit6, y_fit6, label='6 риска', color='red')

# Добавьте легенду для обозначения зависимостей
plt.legend()
plt.ylim(0, None)
plt.xlim(0, None)

# Настройте метки осей и заголовок графика


# Отобразите график


plt.show()

