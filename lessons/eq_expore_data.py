import json 

#Изучеие структуры данных

filename = 'learning_python_erik_matiz\\part_2\\project2_vizualiztion_of_informayion\\lessons\\data\\eq_data_1_day_m1.geojson'

with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'learning_python_erik_matiz\\part_2\\project2_vizualiztion_of_informayion\\lessons\\data\\readable_eq_data.geojson'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4) #аргумент indent=4 приказывает dump() форматрировать данные с
    #отступами, соответсвующим структуре данных

#Построение списка всех землетрясений
all_eq_dicts = all_eq_data['features'] #все землятресения (сколько словорей есть в features)

#Извлечение магнитуд и данных местоположения
mags, lons, lats = [], [], [] #магнитуда, долгота, широта
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag'] #в словаре properties вложен словарь, нас интересуют 
    #значения с ключом mag (магнитуда)
    lon = eq_dict['geometry']['coordinates'][0] #одна долгота = geometry->coordinates->
    #[0], так как дальнейшие данные (сами координаты) записаны не в форме словаря, а в 
    #форме списка
    lat = eq_dict['geometry']['coordinates'][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)