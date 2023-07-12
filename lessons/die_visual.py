from plotly.graph_objects import Bar, Layout
from plotly import offline

from die import Die

#Создание двух кубиков D6
die_1 = Die()
die_2 = Die()

#Моделирование серии бросков с сохранением результатов в списке
results = []
for roll_num in range(1000): #моделируем 1000 бросков кубика
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Анализ результатов
frequencies = []
max_result = die_1.num_sides + die_2.num_sides #максимальный результат 6+6=12
for value in range(2, max_result+1): #для значение от 2 до 12 (т.к. наим. рез-т = 2)
    frequency = results.count(value) #сначала считается кол-во 1, затем 2,...
    frequencies.append(frequency)

#Визуализация результатов в виде гистограммы (столбцовая диаграмма)
x_values = list(range(2, max_result+1)) #все возможные результаты броска кубика.
#т.к. plotly не может получить результат из range напрямую, нам необходимо явно
#преобразовать результат в список с помощью list()
data = [Bar(x=x_values, y=frequencies)] #класс вызываем через скобки списка, так как 
#набор данных может состоять из нескольких элементов. Формотирует данные в виде
#столбцевой диаграммы

#Форматируем оси через список
x_axis_config = {'title': 'Result', 'dtick': 1} #параметр dtick управляет расстоянием
#между делениями на оси оХ
y_axis_config = {'title': 'Frequency of Result'}

#Класс Layout возвращает объект, который задает маакет и конфигурацию диаграммы 
#в целом
my_layout = Layout(title='Results of rolling two D6 dice 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html') #строим график

#Броски кубиков с разным числом граней

#Создание двух кубиков D6 и D10
die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50000): #моделируем 50000 бросков кубика
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Анализ результатов
frequencies = []
max_result = die_1.num_sides + die_2.num_sides #максимальный результат 6+10=16
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
my_layout = Layout(title='Results of rolling a D6 and a D10 50000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')