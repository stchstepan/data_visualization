import json 

from plotly.graph_objects import Scattergeo, Layout #тип диаграмм
from plotly import offline

filename = 'learning_python_erik_matiz\\part_2\\project2_vizualiztion_of_informayion\\lessons\\data\\eq_data_1_day_m1.geojson'

with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'learning_python_erik_matiz\\part_2\\project2_vizualiztion_of_informayion\\lessons\\data\\readable_eq_data.geojson'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

#Построение списка всех землетрясений
all_eq_dicts = all_eq_data['features']

#Извлечение магнитуд и данных местоположения
mags, lons, lats = [], [], [] #магнитуда, долгота, широта
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0] 
    lat = eq_dict['geometry']['coordinates'][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

#Нанесение данных на карту
data = [{'type':'scattergeo', #данные, которые будут нанесены на карту (долгота и широта)
         'lon': lons, 
         'lat': lats,
         'marker': {'size': [5*mag for mag in mags]} #размер маркера увеличивается в зависимости
         #от величины магнитуды землятресения
        }] 
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout} #то, что юудет построенно
offline.plot(fig, filename='global_earthequakes.html')