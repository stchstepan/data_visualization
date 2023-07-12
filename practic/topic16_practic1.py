import csv
from datetime import datetime

from matplotlib import pyplot as plt

#1

filename_sitka = 'learning_python_erik_matiz\\part_2\\project2_vizualiztion_of_informayion\\lessons\\data\\sitka_weather_2021_full.csv'
filename_dv = 'learning_python_erik_matiz\\part_2\\project2_vizualiztion_of_informayion\\lessons\\data\\death_valley_2021_full.csv'

#1.1

with open(filename_sitka) as f_sitka:
    reader = csv.reader(f_sitka)
    header_row = next(reader)

    #Печать заголовков и их позиция
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    #Извлечение и чтение данных
    dates, precipitations = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            precipitation = float(row[5])
        except:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            precipitations.append(precipitation)

#1.2

with open(filename_dv) as f_dv:
    reader = csv.reader(f_dv)
    header_row = next(reader)

    #Печать заголовков и их позиция
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    #Извлечение и чтение данных
    precipitations_dv = []
    for row in reader:
        try:
            precipitation = float(row[3])
        except:
            print(f"Missing data for {current_date}")
        else:
            precipitations_dv.append(precipitation)

#Нанесение данных на диаграмму 
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precipitations, c='blue')
ax.plot(dates, precipitations_dv, c='red')

#Форматирование диаграммы
plt.title("Daily precipitations - 2021\nBlue - Sitka\nRed - Death Valley", fontsize=14)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate() #выводит метки дат по диагонали, чтобы они не перекрывались
plt.ylabel("mm", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

#3

filename_sa = 'learning_python_erik_matiz\\part_2\\project2_vizualiztion_of_informayion\\lessons\\data\\san-francisco_2022_2023_full.csv'

with open(filename_sa) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
    dates, highs, mins = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        try:
            high = int(row[18])
            low = int(row[20])
        except:
            continue
        else:
            dates.append(current_date)
            highs.append(high)
            mins.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, mins, c='blue')
plt.fill_between(dates, highs, mins, facecolor='blue', alpha=0.1)

plt.title("Daily higs and lows - 2021\nSan-Francisco", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("F", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

#4, 5

filename_ny = 'learning_python_erik_matiz\\part_2\\project2_vizualiztion_of_informayion\\lessons\\data\\new_york_2022_2023_full.csv'

files = [filename_sitka, filename_dv, filename_sa, filename_ny]

for file in files:
    with open(file) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        date_index = header_row.index('DATE') #вместо keys, как со словарем
        high_index = header_row.index('TMAX')
        low_index = header_row.index('TMIN')
        name_index = header_row.index('NAME')

        dates, highs, lows = [], [], []

        for row in reader:
            place_name = row[name_index]

            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, color='red', alpha=0.5)
    ax.plot(dates, lows, color='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    
    title = f"Daily High and Low Temperatures, 2021\n{place_name}"
    ax.set_title(title, fontsize=20)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(labelsize=16)
    
    plt.show()