import csv
from datetime import datetime

import plotly.express as px

filename = 'learning_python_erik_matiz\\part_2\\project2_vizualiztion_of_informayion\\lessons\\data\\world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Печать заголовков и их позиция
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    #Извлечение и чтение данных
    dates, lons, lats, brightness = [], [], [], []
    for row in reader:
        try:
            lons.append(row[1])
        except:
            continue
        try:
            lats.append(row[0])
        except:
            continue
        try:
            brightness.append(float(row[2]))
        except:
            continue
        dates.append(datetime.strptime(row[5], '%Y-%m-%d'))

#Нанесение данных на диаграмму 
title = "Worlds fires"
fig = px.scatter_geo(lat=lats, lon=lons, size=brightness, title=title,
        color=brightness,
        color_continuous_scale='Viridis',
        labels={'color':'Brightness'},
        projection='natural earth',
        hover_name=dates,
    )
fig.show()