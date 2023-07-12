import json 

import plotly.express as px

#1, 2

filename = 'learning_python_erik_matiz\\part_2\\project2_vizualiztion_of_informayion\\lessons\\data\\eq_data_30_day_m1.geojson'

with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)

readable_file = 'learning_python_erik_matiz\\part_2\\project2_vizualiztion_of_informayion\\lessons\\data\\readable_eq_data_30_day_m1.geojson'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

#Построение списка всех землетрясений
all_eq_dicts = all_eq_data['features']

#Извлечение магнитуд и данных местоположения
mags, lons, lats, eq_titles  = [], [], [], [] #магнитуда, долгота, широта
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])

#Нанесение данных на карту
title = all_eq_data['metadata']['title']
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
        color=mags,
        color_continuous_scale='Viridis',
        labels={'color':'Magnitude'},
        projection='natural earth',
        hover_name=eq_titles,
    )
fig.show()