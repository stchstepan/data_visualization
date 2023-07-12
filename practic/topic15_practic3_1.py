from plotly.graph_objects import Bar, Layout
from plotly import offline

from die import Die

#1

#Создание двух кубиков D8
die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Анализ результатов
frequencies = []
max_result = die_1.num_sides + die_2.num_sides #максимальный результат 8+8=16
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Визуализация результатов в виде гистограммы (столбцовая диаграмма)
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]


#Форматируем оси через список
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

#Класс Layout возвращает объект, который задает маакет и конфигурацию диаграммы 
#в целом
my_layout = Layout(title='Results of rolling two D8 dice 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')

#2

#Создание трех кубиков D6
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

#Анализ результатов
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides#максимальный результат 18
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Визуализация результатов в виде гистограммы (столбцовая диаграмма)
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]


#Форматируем оси через список
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

#Класс Layout возвращает объект, который задает маакет и конфигурацию диаграммы 
#в целом
my_layout = Layout(title='Results of rolling three D6 dice 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6.html')

#3

#Создание двух кубиков D8
die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

#Анализ результатов
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Визуализация результатов в виде гистограммы (столбцовая диаграмма)
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]


#Форматируем оси через список
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

#Класс Layout возвращает объект, который задает маакет и конфигурацию диаграммы 
#в целом
my_layout = Layout(title='Results of rolling two D8 dice 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8_multuplie.html')
