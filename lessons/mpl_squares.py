import matplotlib.pyplot as plt

#1. Построение простого графика

squares = [1, 4, 9, 16, 25] #данные для нанесения на график

fig, ax = plt.subplots() #функуия subplots() позволяет сгенерировать одну или 
#несколько поддиаграмм на одной диаграмме. Переменная fig представляет рисунок
#или набор генерируемых диаграмм. Переменная ax представляет одну диаграмму на 
#рисунке. 
#fig(Figure) - фигура, ax(axes) - оси.
ax.plot(squares) #строит график на основе заданных значений
plt.show() #открывает окно просмотра Matpolib и выводит график

#2. Изменение типа надписей и толщины графика

squares = [1, 4, 9, 16, 25] #данные для нанесения на график

fig, ax = plt.subplots() 
ax.plot(squares, linewidth=3) #параметр linewidth управляет толщиной строящейся
#линии

#Назначение загаловка диаграммы и меток осей
ax.set_title("Square of Value", fontsize=24) #имя графика и размер шрифта подписи
ax.set_xlabel("Value", fontsize=14) #имя оси Ох и размер шрифта подписи
ax.set_ylabel("Square of Value", fontsize=14) #имя оси Oy и размер шрифта подписи

#Назначение размера шрифта делений на осях
ax.tick_params(axis='both', labelsize=14)  #axis='both' означает, что настройки
#применяются к обеим осям (Ox и Oy); labelsize=14 - размер шрифта для меток деления

plt.show()

#3. Корректировка графика
#Если plot() передается числовая последовательность, функция считает, что первый 
#элемент данных соответствует координате x со значением 0. В примере первая точка
#соответствует значению 1.
#Чтобы такого не было, функции необходимо передать не только квадраты (Oy), 
#но и входные данные (Ox)

input_values = [1, 2, 3, 4, 5] #входные данные (Ox)
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots() 
ax.plot(input_values, squares, linewidth=3) #передаем входные данные (Ox), 
#квадраты (Oy), ...

#Назначение загаловка диаграммы и меток осей
ax.set_title("Square of Value", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Назначение размера шрифта делений на осях
ax.tick_params(axis='both', labelsize=14)

plt.show()

#4. Встроенные стили

print(plt.style.available) #выводит доступные встроенные стили

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn') #использование встроенного стиля
fig, ax = plt.subplots() 
ax.plot(input_values, squares, linewidth=3)

#Назначение загаловка диаграммы и меток осей
ax.set_title("Square of Value", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Назначение размера шрифта делений на осях
ax.tick_params(axis='both', labelsize=14)

plt.show()