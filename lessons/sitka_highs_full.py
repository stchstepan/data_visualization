import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'learning_python_erik_matiz\\part_2\\project2_vizualiztion_of_informayion\\lessons\\data\\sitka_weather_2021_full.csv'
with open(filename) as f:
    reader = csv.reader(f) #создаем объект чтения
    header_row = next(reader) #ф-ия, которая возвращает
    #следующую строку файла для полученного объекта чтения
    #данных 

    #Печать заголовков и их позиция
    for index, column_header in enumerate(header_row): #нумерует каждый элемент списка и возвращает
        #номер и значение элемента
        print(index, column_header)

    #Извлечение и чтение данных
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[7])
        except:
            continue
        try:
            low = int(row[8])
        except:
            continue
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#Нанесение данных на диаграмму 
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) #настройки закрашываемой
#области. Параметр dates - значения по х, параметры highs, lows - значения по y, параметр 
#facecolor - цвет окраски области, параметр alpha - степень прозрачности заливки

#Форматирование диаграммы
plt.title("Daily high and low temperatures - 2021", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate() #выводит метки дат по диагонали, чтобы они не перекрывались
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()