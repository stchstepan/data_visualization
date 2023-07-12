import matplotlib.pyplot as plt

#5. Нанесение и оформление отдельных точек функцией scatter()

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4) #точка (x, y), которую хотим нанести на диаграмму

plt.show()

#5.1. Изменение стиля точки

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200) #аргумент s задает размер точек, используемых 
#в диаграмме

#Назначение загаловка диаграммы и меток осей
ax.set_title("Square of Value", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Назначение размера шрифта делений на осях
ax.tick_params(axis='both', labelsize=14)

plt.show()

#6. Вывод серии точек функцией scatter()
#Для этого необходимо передать список точек функции

x_values = [1, 2, 3, 4, 5] #то, что возводим в квадрат
y_values = [1, 4, 9, 16, 25] #квадраты 

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=200) #передаем списки точек

#Назначение загаловка диаграммы и меток осей
ax.set_title("Square of Value", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Назначение размера шрифта делений на осях
ax.tick_params(axis='both', labelsize=14)

plt.show()

#7. Автоматическое вычисление данных

x_values = list(range(1, 1001)) #список значений от 1 до 1000 (Ox)
y_values = [x**2 for x in x_values] #список значений для Oy, который 
#строится на основе перебора (for x in x_values) и возведения в квадрат 
#(x**2) всех значения из списка значений для Ox

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10) #так как размер данных велик, то
#используется меньший размер точек

#Назначение загаловка диаграммы и меток осей
ax.set_title("Square of Value", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Назначение размера шрифта делений на осях
ax.tick_params(axis='both', labelsize=14)

#Назначение диапазона для каждой оси
ax.axis([0, 1100, 0, 1100000]) #передаются 4 значения в виде списка:
#минимум и максимум по оси Ox (0, 1 100) и минимум и максимум по оси 
#Oy (0, 1 100 000)

plt.show()

#8. Определение пользовательских цветов (стандартных)

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='red', s=200) #для назначения цвета 
#точек в аргумент c в 'одинарные скобки' передается название цвета на 
#английском

#Назначение загаловка диаграммы и меток осей
ax.set_title("Square of Value", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Назначение размера шрифта делений на осях
ax.tick_params(axis='both', labelsize=14)

plt.show()

#8.1. Определение пользовательских цветов (кастомных, в палитр RGB)

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=200) #для назначения 
#кастомного цвета точек в аргумент c в ввиде кортежа передается
#цвет из трех дробных значений от 0 до 1 (r, g, b). Значения, близкие
#к 0 дают более темный оттенок, а к 1 - более светлый

#Назначение загаловка диаграммы и меток осей
ax.set_title("Square of Value", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Назначение размера шрифта делений на осях
ax.tick_params(axis='both', labelsize=14)

plt.show()

#9. Цветовые карты (colormap)
#Представляют собой серию цветов градиента

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) #в с мы 
#передаем список значений по Oy, а затем строчкой cmap=plt.cm.Blues указываем
#цвет градиента

#Назначение загаловка диаграммы и меток осей
ax.set_title("Square of Value", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Назначение размера шрифта делений на осях
ax.tick_params(axis='both', labelsize=14)

#Назначение диапазона для каждой оси
ax.axis([0, 1100, 0, 1100000])

plt.show()

#10. Автоматическое сохранение диаграмм

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#Назначение загаловка диаграммы и меток осей
ax.set_title("Square of Value", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Назначение размера шрифта делений на осях
ax.tick_params(axis='both', labelsize=14)

#Назначение диапазона для каждой оси
ax.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight') #первый аргуент - имя 
#файла, второй - обрезает все лишнее с картинки
