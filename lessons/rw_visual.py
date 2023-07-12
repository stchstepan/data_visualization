import matplotlib.pyplot as plt

from random_walk import RandomWalk

#1. Вывод случайного блуждания

#Построенин случайного блужлания
rw = RandomWalk()
rw.fill_walk()

#Нанесение точек на диаграмму
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)

plt.show()

#2. Генерирование нескольких случайных блужданий

#Новые блуждения строятся до тех пор, пока программа остается активной
while True:
    #Построенин случайного блужлания
    rw = RandomWalk()
    rw.fill_walk()

    #Нанесение точек на диаграмму
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)

    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break

#3. Оформление случайного блуждания

while True:
    #Построенин случайного блужлания
    rw = RandomWalk()
    rw.fill_walk()

    #Нанесение точек на диаграмму
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points) #массив от 1 до 4999
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, 
        edgecolors='none', s=15) #аргумент edgecolors='none' означает, что 
        #мы убираем черный контур вокруг точек

    #Выделение первой и последней точек
    ax.scatter(0, 0, c='green', edgecolors='none', s=100) #начальня точка (0, 0)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100) #конечная точка (последний элемент из списка x_values и y_values)

    #Удаление осей
    ax.get_xaxis().set_visible(False) #Ox
    ax.get_yaxis().set_visible(False) #Oy

    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break

#3.1. Добавление точек

while True:
    #Построенин случайного блужлания
    rw = RandomWalk(50000) #количество точек увеличилось в 10 раз
    rw.fill_walk()

    #Нанесение точек на диаграмму
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9)) #функция figure() управляет шириной,
    #высотой, разрешением и цветом фона диаграммы. Параметр figsize получает кортеж
    #с размерами окна диаграммы в дюймах
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, 
        edgecolors='none', s=1)

    #Выделение первой и последней точек
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100)

    #Удаление осей
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break