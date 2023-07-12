import matplotlib.pyplot as plt

from random_walk import RandomWalk

#1

rw = RandomWalk(5000)
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9)) 

point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=1)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()